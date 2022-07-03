#/bin/bash!

#   If adress already in use 
#   kill -9 $(ps -A | grep python | awk '{print $1}')

#Install dependancies
sudo python3 -m pip install paho-mqtt

#Start program
sudo python3 main.py
