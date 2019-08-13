# This script builds a docker image, pushes it to the registry, applies the k8s configs.
# Prerequisites: 
#                Docker: https://www.docker.com/
#                Running docker registry:  https://docs.docker.com/registry/
#                Installed and configured kubectl: https://kubernetes.io/docs/tasks/tools/install-kubectl/

set -e

if [ "$#" -ne 2 ]; then
    echo "Illegal number of arguments. Usage: deploy.sh docker_registry_url docker_registry_port "
    exit 1
fi

REGISTRY_URL=$1
REGISTRY_PORT=$2

if ! [[ -x "$(command -v docker)" ]]; then
    echo "It seems docker is not installed on your machine."
    echo "Please refer to official web page for instruction on how to install docker."
    echo "https://www.docker.com/"
    exit 1
fi

if ! [[ -x "$(command -v kubectl)" ]]; then
    echo "It seems kubectl is not installed on your machine."
    echo "Please refer to official web page for instruction on how to install kubectl."
    echo "https://kubernetes.io/docs/tasks/tools/install-kubectl/"
    exit 1
fi

# Build docker image
docker build --tag $REGISTRY_URL:$REGISTRY_PORT/inception_service .
echo "Successfully built inception service docker image. "

# Push the image to the registry
docker push $REGISTRY_URL:$REGISTRY_PORT/inception_service
echo "Successfully pushed inception service docker image to registry."

# Apply k8s configs

## Deployment
kubectl apply -f ./kubernates/deployment.yaml

## Service
kubectl apply -f ./kubernates/service.yaml

## Secret
kubectl apply -f ./kubernates/secret.yaml

## Ingress
kubectl apply -f ./kubernates/ingress.yaml

