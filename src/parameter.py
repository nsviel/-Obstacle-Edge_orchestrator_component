#! /usr/bin/python
#---------------------------------------------
#Data and parameters for network connections
#---------------------------------------------

import os


# Parameters
run = True;
gui_width = 600;
gui_height = 650;

# Socket
ip_velo = '127.0.0.1'
ip_edge = '127.0.0.1'
port_velo = 2370 # OUT port
port_pywar = 2370 # IN port
port_edge = 2370 # IN OUT port

# HTTP
http_verbose = False;
http_port = 8888;
http_ip = "";

# MQTT
mqtt_port = 1883;
mqtt_ip = '127.0.0.1';
mqtt_topic = 'ai_obstacle'
mqtt_message = 'hello le monde'

# Path
path_geolocalization = "data/geo.dat"
path_image = "data/image"
