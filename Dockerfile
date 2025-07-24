# Use an official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Copy app files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make realesrgan-ncnn-vulkan binary executable
RUN chmod +x realesrgan-ncnn-vulkan

# Expose port for Flask
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
