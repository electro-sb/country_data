from langchain_community.document_loaders import WebBaseLoader
def webload(url):
    return WebBaseLoader(url)

if __name__=="__main__":
    loader = webload("https://www.scrapethissite.com/pages/simple/")
    print(loader.load().pop().page_content)