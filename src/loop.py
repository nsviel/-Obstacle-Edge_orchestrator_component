#! /usr/bin/python
#---------------------------------------------

from param import param_hu

from src import http
from src import mqtt
from src import connection
from src import socket
from src import file


def start():
    # Init variables
    init()

    # Start main loop program
    while param_hu.run_loop:
        loop()

    # Join threads
    exit()

def init():
    file.init_state()
    http.start_http_daemon()
    mqtt.start_init()
    socket.start_thread_socket_server()
    connection.start_thread_test_conn()

def loop():
    a=1

def exit():
    connection.stop_thread()
