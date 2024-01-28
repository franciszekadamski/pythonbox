# Quick guide
# If you have docker installed in your system:
1. build docker image by running:
```
docker-compose up
```

```
docker build -f Dockerfile.pythonbox -t pythonbox
```
2. run the container from project's directory using docker compose:
```
docker-compose up
```

You can use flag -d to suppress the output.

```
docker-compose up -d
```

You can add flag --build to force build.

```
docker-compose up -d --build
```
## More information
## Configure system for docker container
On Ubuntu:
```
sudo apt update
sudo apt install docker.io
sudo apt install docker-compose
```
or install docker engine.
In case of problems try:
```
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```

Basic test:
```
docker run hello-world
```

On Windows install docker desktop.

## Build docker image from Dockerfile
```
docker build -f Dockerfile.pythonbox -t pythonbox
```

Morover, change the mapping for X11 in the dockerfile if you are using Windows.

## Run the pythonbox using docker-compose
In the directory *pythonbox* containing folder *workspace* run command:
```
docker-compose up
```
or, if there are more than one docker-compose.yml files:
```
docker-compose -f docker-compose-<specific name>.yml
```

When container is running you can log into bash shell using command:
```
docker exec -it pythonbox_1 bash
```

Name of the container can differ depending on the name of the folder. 

For example if the folder has name "dockerized-python" then name of the container will be "dockerized-python_inception_box_1". 

If the folder has name "strawberries" the container will be "strawberries_inception_box_1".

To stop the container press ctrl+v in the interactive console or use command 
```
docker stop pythonbox_1
```
in the terminal. 

