#! /usr/bin/python
#---------------------------------------------

from param import cla

from src import http_server
from src import mqtt
from src import connection
from src import socket_server
from src import file


def start():
    # Init variables
    init()

    # Start main loop program
    while cla.hubium.run_loop:
        loop()

    # Join threads
    end()

def init():
    file.load_configuration()
    http_server.start_daemon()
    mqtt.start_init()
    #socket_server.start_thread_socket_server()
    #connection.start_thread_test_conn()
    cla.hubium.status = "Online"

def loop():
    a=1

def end():
    cla.hubium.status = "Offline"
    file.update_state_file()
    connection.stop_thread()
