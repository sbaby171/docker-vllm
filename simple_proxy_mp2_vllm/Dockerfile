# Proxy Server Dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy proxy server script into the container
COPY proxy_server.py .

# Install required Python libraries
RUN pip install Flask requests

# Expose the port the proxy server will listen on
EXPOSE 5000

# Command to run the proxy server
CMD ["python", "proxy_server.py"]

