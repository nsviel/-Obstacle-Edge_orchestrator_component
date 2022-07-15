#! /usr/bin/python
#---------------------------------------------

from param import param_hu

from conn import http_server
from conn import mqtt_client
from conn import connection
from conn import socket_server

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
    mqtt_client.start_client()
    connection.start_daemon()
    socket_server.start_daemon()
    http_server.start_daemon()
    param_hu.state_hu["self"]["status"] = "Online"

def loop():
    a=1

def end():
    param_hu.state_hu["self"]["status"] = "Offline"
    parser_json.upload_file(param_hu.path_state_hu, param_hu.state_hu)
    connection.stop_daemon()
    socket_server.stop_daemon()
    http_server.stop_daemon()
