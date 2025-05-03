FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies (optional but recommended for common issues)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Copy .env file
COPY .env .env

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose port (optional, for documentation)
EXPOSE 8080

# Run Gunicorn with Flask
CMD ["gunicorn", "-b", "0.0.0.0:8080", "--threads=4", "app:app"]
