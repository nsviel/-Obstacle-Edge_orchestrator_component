#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from HTTP import http_client_fct

import http.client as client
import json


def post_param_py(payload):
    if(param_hu.state_hu["pywardium"]["http_connected"]):
        http_client_fct.send_post_request_py("/new_param_py", payload)

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
