#! /usr/bin/python
#---------------------------------------------

from param import param_hu

import http.client as client
import requests


def test_py_connection():
    ip = param_hu.state_hu["pywardium"]["ip"]
    port = param_hu.state_hu["pywardium"]["http_server_port"]

    if(http_connection(ip, port, "/test_http_conn")):
        param_hu.state_hu["pywardium"]["connected"] = True
    else:
        connection_closed()

def http_connection(ip, port, get):
    connected = False
    sock = client.HTTPConnection(ip, port, timeout=0.1)
    try:
        sock.request("GET", get)
        connected = True
    except:
        connected = False
    sock.close()
    return connected

def connection_closed():
    param_hu.state_hu["pywardium"]["connected"] = False
    param_hu.state_py["lidar_1"]["connected"] = False
    param_hu.state_py["lidar_2"]["connected"] = False
