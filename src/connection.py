#! /usr/bin/python
#---------------------------------------------

from param import param_hu

from src import mqtt
from src import parser_json
from src import socket_client
from src import http_client
from src import io

from threading import Thread

import time


def start_daemon():
    thread_con = Thread(target = thread_test_connection)
    thread_con.start()

def thread_test_connection():
    param_hu.run_thread_con = True
    while param_hu.run_thread_con:
        # Test connection
        mqtt.test_connection()
        socket_client.test_velo_connection()
        http_client.test_connection()

        # Update state file
        parser_json.upload_file(param_hu.path_state_hu, param_hu.state_hu)

        # Wait for 1 second
        time.sleep(1)
        pass

def stop_thread():
    param_hu.run_thread_con = False
    param_hu.run_thread_socket = False
