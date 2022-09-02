#/bin/bash!

#   If adress already in use 
#   kill -9 $(ps -A | grep python | awk '{print $1}')

#Install dependancies
sudo apt install python3 python3-scapy python3-pcapy
pip install paho-mqtt
sudo pip3 install requests

#Start program
sudo python3 main.py
