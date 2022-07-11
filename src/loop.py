#! /usr/bin/python
#---------------------------------------------

from param import classes

from src import http_server
from src import mqtt
from src import connection
from src import socket_server
from src import file


def start():
    # Init variables
    init()

    # Start main loop program
    while classes.hubium.run_loop:
        loop()

    # Join threads
    end()

def init():
    file.init_state()
    http_server.start_http_daemon()
    mqtt.start_init()
    socket_server.start_thread_socket_server()
    connection.start_thread_test_conn()
    classes.hubium.status = "Online"

def loop():
    a=1

def end():
    classes.hubium.status = "Offline"
    file.update_state_file()
    connection.stop_thread()
