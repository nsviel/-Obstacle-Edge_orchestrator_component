#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import mqtt

from threading import Thread

import json
import time


def test_connection():
    while parameter.thread_con:
        mqtt.test_connection()
        update_state_json()
        time.sleep(1)
        pass

def start_thread_test_conn():
    parameter.thread_con = True
    thread_con = Thread(target = test_connection)
    thread_con.start()

def stop_thread():
    parameter.thread_con = False

def update_state_json():
    file = open('src/state.json', "r")
    data = json.load(file)
    if(data["mqtt"]["connected"] != parameter.mqtt_connected):
        data["mqtt"]["connected"] = parameter.mqtt_connected
        file = open('src/state.json', "w")
        json.dump(data, file, indent=4)
        file.truncate()
