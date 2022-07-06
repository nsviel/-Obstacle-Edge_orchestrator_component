#! /usr/bin/python
#---------------------------------------------
#Data and parameters for network connections
#---------------------------------------------

import os

import paho.mqtt.client as mqtt


#Pywardium
py_ip = ""
py_sock_port = 1

# Velodium
velo_connected = False
velo_ip = '127.0.0.1'
velo_port = 1

# AI
ai_connected = False

# Sncf
mqtt_connected = False
mqtt_client  = None
mqtt_ip = '127.0.0.1'
mqtt_port = 1
mqtt_topic = 'ai_obstacle'
mqtt_message = 'hello world'

# Valeo
valeo_ip = '127.0.0.1'
valeo_port = 1

# Edge
edge_ip = '127.0.0.1'
edge_port = 1
