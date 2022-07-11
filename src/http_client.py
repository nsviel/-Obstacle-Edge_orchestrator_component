#! /usr/bin/python
#---------------------------------------------


from param import classes

import http.client as client
import requests


def test_connection():
    sock = client.HTTPConnection(classes.connec.py_ip, classes.connec.py_http_port, timeout=0.1)
    try:
        sock.request("GET", "/test")
        classes.connec.py_http_connected = True
    except:
        connection_closed()
    sock.close()

def connection_closed():
    classes.connec.py_http_connected = False
