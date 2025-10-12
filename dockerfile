FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

# Copy dependency files
COPY pyproject.toml uv.lock /app/

# Install dependencies using uv
RUN uv pip install --system -r pyproject.toml

# Copy application code
COPY . /app

# Expose the port the app runs on
EXPOSE 8000

# Run the FastAPI application with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

