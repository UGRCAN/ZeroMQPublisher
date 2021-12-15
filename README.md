# ZeroMQPublisher
Messaging System

## Overview
Example repository to demonstrate how you can turn Python scripts into micro-services in Docker containers,
which can communicate over ZeroMQ. The examples here can be run as just Docker-Docker (docker run). 

Examples are using a Publisher-Subscriber pattern to communicate. This means that the publisher micro-service just send messages out to a port, without knowing who is listening and a subscriber micro-service receiving data with topic.

In this example, publisher is considered as server and subscriber as client. 

The reason why I prefer ZeroMQ from MQ systems is that ZeroMQ can provide the messaging system without the need for any broker. For alternatives, see: RabbitMQ

## Install Docker
  Installing Docker is required.

* [General Docker instructions](https://docs.docker.com/install/#supported-platforms)
* [Docker Toolbox for Windows 7/8/10 Home](https://docs.docker.com/toolbox/overview/)
* [Docker for Windows 10  Pro, Enterprise or Education](https://docs.docker.com/docker-for-windows/install/#what-to-know-before-you-install)
* Ubuntu: [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) and [docker-compose](https://docs.docker.com/compose/install/) and `sudo usermod -a -G docker $USER`

Notes:
Client side (C#) prepared for Windows Containers. If you are going to use the subscriber image I prepared, after installed docker please switch Linux Docker Container to Windows Docker Container.

 ## Docker-Docker Communication with docker run
 
 1. Open a terminal and navigate to folder ZeroMQPublisher-master
 2. Execute `docker build -t publisher .` to create Docker image. It may take a while.
 3. Execute `docker run -it -p 1234:1234 --name publisher publisher`
 4. Now, your publisher container started to run.
 5. Open another terminal to pull Subscriber image. Execute `docker pull ugurcan10/subscriber`
 6. Execute `docker run ugurcan10\subscriber --name subscriber`
 7. After both containers are up, from the terminal where you open the publisher container, type your message and press enter and view the message you wrote from the subscriber container.
 
 Notes:
 * Step 3 command is important. (-it is interactive mode, -p is port binding, --name is container name (container name must be "publisher", subscriber containers will bind name to container ip) , last publisher is image name to run)
 * Subscriber image is registered in my dockerhub account. Alternatively, If you want to download subscriber's source code, create and run a docker image, you can download the project from https://github.com/UGRCAN/ZeroMQSubscriber , then navigate to project folder and
   *  Execute  `docker build -t subscriber .` 
   * Execute `docker run --name subscriber subscriber`
