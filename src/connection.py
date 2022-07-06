#! /usr/bin/python
#---------------------------------------------

from param import param_hu

from src import mqtt
from src import socket
from src import file

from threading import Thread

import json
import time


def thread_test_connection():
    while param_hu.run_thread_con:
        mqtt.test_connection()
        socket.test_connection()
        file.update_state_file()
        time.sleep(1)
        pass

def start_thread_test_conn():
    param_hu.run_thread_con = True
    thread_con = Thread(target = thread_test_connection)
    thread_con.start()

def stop_thread():
    param_hu.run_thread_con = False
    param_hu.run_thread_socket = False
