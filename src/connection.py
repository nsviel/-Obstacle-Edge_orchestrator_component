#! /usr/bin/python
#---------------------------------------------

from param import param_hu

from HTTP import http_client
from HTTP import http_client_get
from MQTT import mqtt_client
from SOCK import sock_client

from src import parser_json
from src import io

from threading import Thread

import threading
import time


def start_daemon():
    thread_con = Thread(target = thread_test_connection)
    thread_con.start()

def stop_daemon():
    param_hu.run_thread_con = False

def thread_test_connection():
    param_hu.run_thread_con = True
    while param_hu.run_thread_con:
        # Test connection
        mqtt_client.test_sncf_connection()
        sock_client.test_velo_connection()
        http_client.test_py_connection()

        # Update state file
        http_client_get.get_state_py()
        parser_json.upload_state()
        update_nb_thread()

        # Wait for 1 second
        time.sleep(1)
        pass

def update_nb_thread():
    param_hu.state_hu["self"]["nb_thread"] = threading.active_count()
