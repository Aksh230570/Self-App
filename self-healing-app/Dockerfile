# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency file and install
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app/ .

# Expose port
EXPOSE 5000

# Run app
CMD ["python", "app.py"]
