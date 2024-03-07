#!/bin/bash

# Define image name
IMAGE_NAME="atm_data_seeder"

# Build the Docker image
docker build -t $IMAGE_NAME .

# Start the container in detached mode
docker run -d \
  --name atm_data_seeder_container \
  $IMAGE_NAME

# Print confirmation message
echo "ATM data seeder deployed successfully."
