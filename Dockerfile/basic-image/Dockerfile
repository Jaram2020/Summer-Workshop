ARG distro=stretch
FROM resin/rpi-raspbian:$distro

RUN apt-get update
RUN apt-get install python3 python3-dev python3-pip
RUN sudo apt-get install build-essential
RUN sudo apt-get install gdb-multiarch