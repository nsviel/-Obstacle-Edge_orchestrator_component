#! /usr/bin/python
#---------------------------------------------

from src import http
from src import mqtt
from src import parameter
from src import connection

from gui import gui_loop


def init():
    http.connect()
    connection.start_thread_test_conn()

def loop():
    a=1

def exit():
    connection.stop_thread()
