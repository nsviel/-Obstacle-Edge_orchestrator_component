#!/bin/sh


#Build all sub-containers (equ. docker run)
sudo docker-compose up --no-build --abort-on-container-exit
