#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import mqtt

from threading import Thread

import json
import time


def test_connection():
    while parameter.run_thread_con:
        mqtt.test_connection()
        time.sleep(1)
        pass

def start_thread_test_conn():
    parameter.run_thread_con = True
    thread_con = Thread(target = test_connection)
    thread_con.start()

def stop_thread():
    parameter.run_thread_con = False
