#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from HTTP import http_client_fct

import http.client
import json


def post_param_py(payload):
    connected = param_hu.state_hu["pywardium"]["http_connected"]
    if(connected):
        ip = param_hu.state_hu["pywardium"]["ip"]
        port = param_hu.state_hu["pywardium"]["http_server_port"]
        header = {"Content-type": "application/json"}
        if(connected):
            try:
                client = http.client.HTTPConnection(ip, port, timeout=1)
                client.request("POST", "/new_param_py", payload, header)
                client.close()
            except:
                print("[\033[1;31merror\033[0m] Command \033[1;36m%s\033[0m to ip \033[1;36m%s\033[0m port \033[1;36m%d\033[0m failed" % (command, ip, port))

def post_param_ai(command, value):
    connected = param_hu.state_hu["velodium"]["http_connected"]
    port = param_hu.state_hu["velodium"]["http_server_port"]
    header = {"Content-type": "application/json"}
    if(connected):
        try:
            client = http.client.HTTPConnection("localhost", port, timeout=1)
            client.request("POST", command, value, header)
            client.close()
        except:
            print("[\033[1;31merror\033[0m] Command \033[1;36m%s\033[0m to ip \033[1;36m%s\033[0m port \033[1;36m%d\033[0m failed" % (command, ip, port))


def send_py_state(data):
    # Parameters
    ip = param_hu.state_hu["pywardium"]["ip"]
    port = param_hu.state_hu["pywardium"]["http_server_port"]
    connected = param_hu.state_hu["pywardium"]["http_connected"]

    # Header
    header = {"Content-type": "application/json"}
    command = "/new_state_py"

    if(connected):
        try:
            client = http.client.HTTPConnection(ip, port, timeout=1)
            client.request("POST", command, data, header)
            client.close()
        except:
            print("[\033[1;31merror\033[0m] Command \033[1;36m%s\033[0m to ip \033[1;36m%s\033[0m port \033[1;36m%d\033[0m failed" % (command, ip, port))
