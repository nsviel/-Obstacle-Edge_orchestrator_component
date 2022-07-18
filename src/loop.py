#! /usr/bin/python
#---------------------------------------------

from param import param_hu

from HTTP import http_server
from MQTT import mqtt_client
from SOCK import socket_server

from src import connection
from src import state
from src import parser_json
from src import data


def start():
    # Init variables
    init()

    # Start main loop program
    while param_hu.run_loop:
        loop()

    # Join threads
    end()

def init():
    data.check_directories()
    state.load_configuration()
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
