#! /usr/bin/python
#---------------------------------------------

from param import param_hu

from src import http_server
from src import mqtt
from src import connection
from src import socket_server
from src import file
from src import parser_json


def start():
    # Init variables
    init()

    # Start main loop program
    while param_hu.run_loop:
        loop()

    # Join threads
    end()

def init():
    file.load_configuration()
    http_server.start_daemon()
    mqtt.start_client()
    socket_server.start_daemon()
    connection.start_daemon()
    param_hu.state_hu["self"]["status"] = "Online"

def loop():
    a=1

def end():
    param_hu.state_hu["self"]["status"] = "Offline"
    parser_json.upload_file(param_hu.path_state_hu, param_hu.state_hu)
    connection.stop_thread()
