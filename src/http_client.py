#! /usr/bin/python
#---------------------------------------------

from param import param_ext
from param import param_ext

import http.client as client

import requests


def test_connection():
    sock = client.HTTPConnection(param_hu.py_ip, param_hu.py_http_port, timeout=0.1)
    try:
        sock.request("GET", "/test")
        param_ext.py_http_connected = True
    except:

        connection_closed()
    sock.close()

def connection_closed():
    param_ext.py_http_connected = False
