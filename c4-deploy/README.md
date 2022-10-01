# Some info

## Requirements

- Install Docker
    - For windows: [Download](https://docs.docker.com/desktop/install/windows-install/)
    - For Ubuntu and WSL Run:
        ```
        sudo snap install docker
        ```
    - For other linux distros: [See here](https://docs.docker.com/engine/install/ubuntu/)

## Checklist - What do we need to do

- [ ] Containerize the application
    - [ ] Create a Dockerfile
        - [Dockerfile docs](https://docs.docker.com/engine/reference/builder/)
        - [ ] Define a `.dockerignore` to ignore file you don't need in your image
    - [ ] Build the docker image
        Run:
        ```sh
        docker build -t ${IMAGE_NAME}:${IMAGETAG} .
        ```
    - [ ] Run the docker image
        Run:
        ```
        docker run -p $HOST_PORT:$CONTAINER_PORT $IMAGE_NAME
        ```
        Example:
        ```
        ```

## Setting up kubernetes

[Kubernetes docs](https://kubernetes.io/docs/home/)

[Minkube](https://minikube.sigs.k8s.io/docs/start/) for running kubernetes locally
[kubectl]()
    - Ubuntu & WSL: `sudo snap install kubectl --classic`
    - Kubectl also comes with docker desktop
[K8Slens - Kubectl UI tool](https://k8slens.dev/)