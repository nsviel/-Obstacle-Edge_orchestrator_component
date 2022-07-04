#! /usr/bin/python
#---------------------------------------------
#Data and parameters for network connections
#---------------------------------------------

import os

import paho.mqtt.client as mqtt


# Thread
run_loop = True
run_thread_con = False

# Velodium
velo_ip = '127.0.0.1'
velo_port = 2370

# Edge
edge_ip = '127.0.0.1'
edge_port = 2370

# Pywardium
py_port_sock = 2370

# Valeo
valeo_ip = '127.0.0.1'
valeo_port = 2370

# HTTP daemon
http_verbose = False
http_port = 8000;
http_ip = "";

# MQTT
mqtt_connected = False
mqtt_client  = None
mqtt_ip = '127.0.0.1'
mqtt_port = 1883
mqtt_topic = 'ai_obstacle'
mqtt_message = 'hello world'

# Path
path_state = "src/state.json"
path_geoloc = "data/geo.dat"
path_image = "data/image/image"
path_frame = "data/frame/"
path_predic = "data/prediction/"
path_generic = "data/generic/"
