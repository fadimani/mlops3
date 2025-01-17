# Use an official Python 3.10 base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY ./mlruns /app/mlruns
COPY ./mission_4.py /app/mission_4.py


# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir fastapi uvicorn mlflow pandas pydantic psutil

# Expose the application's port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "mission_4:app", "--host", "0.0.0.0", "--port", "8000"]