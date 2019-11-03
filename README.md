# Robot from Mars

Simple robot controller of robot.

## Technologies
Solution created using python 3.6.7 and the following technologies:
- [Pytest](https://docs.pytest.org/en/latest/)-Framework to writte tests for applications and libraries.

## Running solution with Docker

If you want to run this solution without install anything (except docker)  on your machine, you must to use docker to run this solution. To build this solution with docker, you need to install it before (please refeer to [official docker docs](https://docs.docker.com/install/)).

Due to the fact that the requirements contains only the necessary to run this solution, the docker image uses Linux Alpine 3.7.

To build the container follow the steps:

1. Go to the root of the project
>$ cd ../

2. Build the docker image (this will install all the listed dependencies on requirements)
>$ docker-compose build

3. Run app by executing container:
>$ docker-compose up

## Usage

1. In another terminal execute the following command to access the container bash. You must list all the containers running, then you have to get your container id:
>$ docker ps

2. Then, with your id, you use the following command to connect in the terminal:
>$ docker exec -it b052349321b4 ash

3. To see all arguments accepted by the application type:
>$ python run.py -h

3. To run the commands text of your robots type on terminal:
>$ python run.py -file example_file.txt

The output with the final coordinates of your robot will be shoed on the terminal

### WARNING
**If the commands in yout file moves to a coordinate outside the plateau dimensions a error will be showed in your terminal**


## Improvements/Features

* Graphical interface to visualize the path traveled by robots
