# Set the python image version
FROM python:3.12-slim

# Install system dependencies and Poetry
RUN apt update && apt install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt clean && rm -rf /var/lib/apt/lists/*

# Set Poetry environment paths
ENV PATH="/root/.local/bin:$PATH"

# Set working directory inside the container
WORKDIR /app

# Copy pyproject.toml and poetry.lock first to leverage Docker caching
COPY pyproject.toml poetry.lock ./

# Copy data, models and fastapi folders
COPY ./data /app/data
COPY ./models /app/models
COPY ./fastapi /app/fastapi

# Install project dependencies (without virtualenv)
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Expose port 8000 (FastAPI default)
EXPOSE 8000

# Run the FastAPI backend in production mode
CMD ["fastapi", "run", "fastapi/app.py"]
