#! /usr/bin/python
#---------------------------------------------

from param import classes

from src import mqtt
from src import socket
from src import file
from src import http_client

from threading import Thread

import time


def thread_test_connection():
    classes.hubium.run_thread_con = True
    while classes.hubium.run_thread_con:
        # Test connection
        mqtt.test_connection()
        socket.test_connection()
        http_client.test_connection()

        # Update state
        file.update_state_file()

        # Wait for 1 second
        time.sleep(1)
        pass

def start_thread_test_conn():
    thread_con = Thread(target = thread_test_connection)
    thread_con.start()

def stop_thread():
    classes.hubium.run_thread_con = False
    classes.hubium.run_thread_socket = False
