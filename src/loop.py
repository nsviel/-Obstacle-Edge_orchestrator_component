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
    while parameter.run:
        loop()

    # Join threads
    exit()

def init():
    http.connect()
    mqtt.connect()
    connection.start_thread_test_conn()

def loop():
    a=1

def exit():
    connection.stop_thread()
