# Pull image with python uv
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
# maintainer:
LABEL maintainer="electronic.sapience@gmail.com"
# Copy application files
COPY . /app
# Set working directory
WORKDIR /app
# Install dependencies
#RUN ["uv", "install", "project.toml"]
# Expose port
EXPOSE 8501
# Start the application
ENTRYPOINT ["uv", "run", "streamlit", "run", "main.py","--server.port=8501", "--server.address=0.0.0.0"]
