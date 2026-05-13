# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Create working folder and install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application contents
COPY service/ ./service/

# Switch to a non-root user
RUN useradd --uid 1000 theia && chown -R theia /app
USER theia

# Expose the port the app runs on
EXPOSE 8080

# Run gunicorn to serve the microservice
CMD ["gunicorn", "--bind=0.0.0.0:8080", "--log-level=info", "service:app"]
