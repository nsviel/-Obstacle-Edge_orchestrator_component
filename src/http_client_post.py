#! /usr/bin/python
#---------------------------------------------

from param import param_hu

import http.client as client
import json


def post_new_state_py():
    connected = param_hu.state_hu["pywardium"]["connected"]
    ip = param_hu.state_hu["pywardium"]["ip"]
    port = param_hu.state_hu["pywardium"]["http_server_port"]
    header = {"Content-type": "application/json"}
    file = json.dumps(param_hu.state_py)
    if(connected):
        try:
            sock = client.HTTPConnection(ip, port, timeout=1)
            sock.request("POST", "/new_state_py", file, header)
            sock.close()
        except:
            print("[error] Sending new state py failed for ip: %s | port: %d"% (ip, port))
