#! /usr/bin/python
#---------------------------------------------

from src import http
from src import mqtt
from src import callback
from src import parameter


def init():
    mqtt.connect()
    http.connect()

def loop():
    callback.callback_loop()
