#! /usr/bin/python
#---------------------------------------------

from param import cla

from src import mqtt
from src import file
from src import socket_client
from src import http_client
from src import io

from threading import Thread

import time


def start_daemon():
    thread_con = Thread(target = thread_test_connection)
    thread_con.start()

def thread_test_connection():
    cla.hubium.run_thread_con = True
    while cla.hubium.run_thread_con:
        # Test connection
        mqtt.test_connection()
        socket_client.test_velo_connection()
        http_client.test_connection()

        # Update state
        file.update_data_file()
        file.update_state_file()

        # Wait for 1 second
        time.sleep(1)
        pass

def stop_thread():
    cla.hubium.run_thread_con = False
    cla.hubium.run_thread_socket = False
