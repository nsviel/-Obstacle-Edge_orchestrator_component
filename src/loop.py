#! /usr/bin/python
#---------------------------------------------

from src import http
from src import mqtt
from src import parameter
from src import connection


def start():
    # Init variables
    init()

    # Start main loop program
    while parameter.run_loop:
        loop()

    # Join threads
    exit()

def init():
    http.start_http_daemon()
    mqtt.start_init()
    connection.start_thread_test_conn()

def loop():
    a=1

def exit():
    connection.stop_thread()
