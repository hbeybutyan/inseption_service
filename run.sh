# This script builds and runs a docker image
# Prerequisites: 
#                Docker: https://www.docker.com/

set -e
# Buid docker image
docker build --tag inception_service .
echo "Successfully built inception service docker container. Running "

# Run container
docker run -d -p 5000:5000 inception_service
echo "Inception service running in container. Use port 5000 to access it."

echo "Please refer to documentation/github repo for further instructions on service usage."
echo "https://github.com/hbeybutyan/inseption_service"
