#! /usr/bin/python
#---------------------------------------------


from param import param_hu

import http.client as client
import requests


def test_connection():
    ip = param_hu.state_hu["pywardium"]["ip"]
    port = param_hu.state_hu["pywardium"]["http_server_port"]
    sock = client.HTTPConnection(ip, port, timeout=0.1)
    try:
        sock.request("GET", "/test")
        param_hu.state_hu["pywardium"]["connected"] = True
    except:
        connection_closed()
    sock.close()

def connection_closed():
    param_hu.state_hu["pywardium"]["connected"] = False
    param_hu.state_py["lidar_1"]["connected"] = False
    param_hu.state_py["lidar_2"]["connected"] = False
