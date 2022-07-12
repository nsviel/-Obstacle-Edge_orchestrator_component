#! /usr/bin/python
#---------------------------------------------


from param import cla

import http.client as client
import requests


def test_connection():
    sock = client.HTTPConnection(cla.connec.py_ip, cla.connec.py_http_server_port, timeout=0.1)
    try:
        sock.request("GET", "/test")
        cla.connec.py_http_connected = True
    except:
        connection_closed()
    sock.close()

def connection_closed():
    cla.connec.py_http_connected = False
