#! /usr/bin/python
#---------------------------------------------
#Data and parameters for network connections
#---------------------------------------------

import os

import paho.mqtt.client as mqtt


# State
#--------------------
status = "Offline"
ip = "127.0.0.1"
#--------------------

# Thread
run_loop = True
run_thread_con = False
run_thread_socket = False

# Socket
sock_server = None
sock_port = 1
sock_port_listen = 1
sock_port_connection = 1

# HTTP daemon
httpd_verbose = False
httpd_port = 8000;
httpd_ip = "";

# Path
path_state = "param/state.json"
path_config = "param/config.json"
path_geoloc = "data/geo.dat"
path_image = "data/image/image"
path_frame = "data/frame/"
path_predic = "data/prediction/"
path_generic = "data/generic/"
