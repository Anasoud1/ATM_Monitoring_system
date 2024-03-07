# Base image
FROM python:3.9

# Create work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Set database environment variables
ENV DB_USER=${DB_USER}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DB_HOST=${DB_HOST}
ENV DB_NAME=${DB_NAME}

# Set working directory in Python script
CMD ["python", "-m", "atm_data_seeder", "/app/dummy.json"]

# Expose port
EXPOSE 5555