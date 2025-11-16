from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.tools import DuckDuckGoSearchResults
from langchain.chains import LLMChain, SequentialChain
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
import webscrapper
import pandas as pd
import numpy as np
import streamlit as st
import os

 #os.environ[\"GROQ_API_KEY\"] = getpass.getpass(\"key :\")
# if "GROQ_API_KEY" not in os.environ:
#     os.environ["GROQ_API_KEY"] = keys.get_keys('groq')
#Creating the llm prompt
load_dotenv()

llm = ChatGroq(
    model= "llama-3.3-70b-versatile",
    temperature= 0,
    api_key= os.getenv("GROQ_API_KEY"),
    max_tokens= None,
    timeout= None,
    max_retries= 2
)
llm.bind_tools([DuckDuckGoSearchResults(k=2)])


country_extract = PromptTemplate.from_template(
    """
    ### SCRAPED TEXT FROM WEBSITE:
    (page data)
    ### INSTRUCTION:
    The scraped page is from list of national capital page from a website.
    your job is to extract the country data and return them in json format containing
    following keys: 'Country', 'Capital', and 'Continent'.
    Only return valid JSON.
    ### VALID JSON (NO PREAMBLE): 
    """
)

llm_chain_country_data = LLMChain(llm=llm, prompt=country_extract, output_key= 'Country')

prompt_country_Data = PromptTemplate(
    input_variables= ["Country"],
    template= """
    ### INSTRUCTION:
    Please provide information about {Country} that should contain the following keys:
    'Population', 'GDP', 'GDP per capita', 'Area', 'Currency', 'Languages','Other Major Cities', 'Attraction', 'Climate','Timezone'
    ###(NO PREAMBLE): 
    """ 
)

prompt_city_coordinate= PromptTemplate(
    input_variables= ["Capital"],
    template= """
    ### INSTRUCTION:
    Please provide the latitude and longitude of {Capital} in JSON format.
    ###VALID JSON(NO PREAMBLE): 
    """
)


llm_chain_country_characteristics = LLMChain(llm=llm, prompt=prompt_country_Data, 
                                    output_key= "country_characteristics")    

chain_llm = country_extract |llm
# chain_llm = SequentialChain(chains=[llm_chain_country_data, llm_chain_country_characteristics], 
#                             input_variables= ["Country"],
#                             output_variables= ["country_data", "country_characteristics"])

if __name__=="__main__":
    st.title(":rainbow[Country Information]✈️")
    left,mid,right = st.columns([4,4,1])
    with left:
        st.markdown("""**:orange[⚡llama-3.3-70b-versatile]**""")
    with mid:
        st.markdown("""**:violet[⚡Langchain GROQ API]**""") 
    with right:
        btn = st.button(":orange[🔃]", type="tertiary", use_container_width=True)

    os_path = os.path.join(os.getcwd(), '/data/country_data.csv')
    json_parser= JsonOutputParser()
    if btn or not (os.path.exists(os_path)):
        loader = WebBaseLoader("https://en.wikipedia.org/wiki/List_of_national_capitals")
        #"https://www.scrapethissite.com/pages/simple/"
        page_data = loader.load().pop().page_content
        #Get the country information in a clean JSON
        #print(page_data)

    if os.path.exists(os_path):
        df = pd.read_csv(os_path)
    else:
        country_res= chain_llm.invoke(input= {'page_data': page_data} )#
        #country_res= chain_llm(input= {'Country': 'India'} )
        #Print the JSON file
        #print(json_parser.parse(country_res.content))
        df = pd.DataFrame(json_parser.parse(country_res.content))
        save_path = os.path.join('./country_data.csv')
        df.to_csv(save_path, index=False)

    st.sidebar.title(":rainbow[Country Selection] 🌎")
    random = np.random.randint(0, len(df['Country']))
    country_name = st.sidebar.selectbox(":orange[Select Country from the dropdown:]", df['Country'])#,index=random
    #print(country_name) #to be enabled to print the output at terminal
    c_Data = df[df['Country'] == country_name]
    #st.divider()
    st.table(c_Data)
    other_data = prompt_country_Data|llm
    country_data = other_data.invoke({'Country': country_name})
    st.write(country_data.content)
    capital_data = prompt_city_coordinate|llm
    data_capital = capital_data.invoke({'Capital': c_Data.iloc[0]['Capital']})
    pd_capital = pd.DataFrame(json_parser.parse(data_capital.content), index= [0])
    st.sidebar.map(pd_capital, zoom=1, color='#00ff00', width=250, height=250)
    #st.sidebar.write(pd_capital)

    # print(os.getcwd())
    # # data = pd.DataFrame({'Country': ['India', 'China', 'USA'], 
    # #                     'Capital': ['New Delhi', 'Beijing', 'Washington D.C.'], 
    # #                     'Continent': ['Asia', 'Asia', 'North America']})
    # path = os.path.join(os.getcwd(), "data\ptest_data.csv")
    # print(path)
    # # data.to_csv(path, index=False)
