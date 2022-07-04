#! /usr/bin/python
#---------------------------------------------
#Data and parameters for network connections
#---------------------------------------------

import os

import paho.mqtt.client as mqtt


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

thread_con = False

# HTTP
http_verbose = False
http_is_connected = False
http_port = 8000;
http_ip = "";

# MQTT
mqtt_connected = False
mqtt_client  = None
mqtt_port = 1883
mqtt_ip = '127.0.0.1'
mqtt_topic = 'ai_obstacle'
mqtt_message = 'hello world'

# Path
path_geoloc = "data/geo.dat"
path_image = "data/image/image"
path_frame = "data/frame/"
path_predic = "data/prediction/"
path_generic = "data/generic/"
