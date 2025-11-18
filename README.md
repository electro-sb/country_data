[![Profile](./assets/badges/profile.svg)](https://github.com/electro-sb)
###### Project Information:
<!--- Badges --->
[![Project](./assets/badges/Project.svg)](./README.md)
[![Version](./assets/badges/version.svg)](./pyproject.toml)
###### Metadata:
<!--- Badges --->
[![Git Commit](./assets/badges/git.svg)](./README.md)
[![Last Updated](./assets/badges/updated.svg)](./README.md)
[![Build Status](./assets/badges/actions.svg)](./pyproject.toml)
###### Documentation:
<!--- Badges --->
[![Documentation](./assets/badges/docs.svg)](./README.md)
###### License:
<!--- Badges --->
[![License](./assets/badges/license.svg)](./LICENSE.md)


# Country Data Project

This project provides tools for scraping, analyzing, and visualizing country-related data. It includes the following components:

## Features

- **Data Processing**: Core functions and classes for handling country data.
- **Web Scraping**: Tools for fetching and parsing data from various sources.
- **Containerization**: Docker support for consistent deployment environments, including Docker Compose.
- **Streamlit Integration**: Option to run a Streamlit app for interactive data visualization.

## Files Overview

- **`country_data.py`**: Core module for data operations.
- **`webscrapper.py`**: Script for scraping country-related data.
- **`Dockerfile`**: Defines steps to build a Docker image for the project.
- **`docker-compose.yml`**: Configuration file for Docker Compose.
- **`pyproject.toml`**: Manages the build system and dependencies.

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/country_data.git
    cd country_data
    ```
2. Create a `.env` file in the project directory and add your API key:
    ```bash
    GROQ_API_KEY=your_api_key_here
    ```
3. Build and run the Docker container (optional):
    ```bash
    docker build -t sudipto19/country_data .
    docker run -it --env-file=/home/<path_to_project>/country_data/.env sudipto19/country_data
    ```
   Or run in detached mode:
    ```bash
    docker run -d --env-file=/home/<path_to_project>/country_data/.env sudipto19/country_data
    ```

4. Use Docker Compose for easier container management (optional):
    - Build and start the services:
        ```bash
        docker compose up --build
        ```
    - if imahge is available
        docker compose pull
        docker compose up -no-build
        ```
    - Start the services without rebuilding:
        ```bash
        docker compose up
        ```
    - Stop and remove the services:
        ```bash
        docker compose down
        ```

5. Run the Streamlit app directly (optional):
    ```bash
    uv run streamlit run main.py
    ```

## Requirements

- Python 3.x
- Docker (optional)
- Docker Compose (optional)
- Dependencies listed in `pyproject.toml`

## Output Example

![Country Data Visualization](image-1.png)

## License

This project is licensed under the MIT License. See the[LICENSE](./LICENSE.md) file for more details.
