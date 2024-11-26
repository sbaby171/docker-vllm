# Base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY app/ /app/

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose Flask port
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
