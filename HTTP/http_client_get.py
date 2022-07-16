#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from HTTP import http_client
from src import parser_json

import http.client as client
import requests


def get_state_py():
    connected = param_hu.state_hu["pywardium"]["connected"]
    ip = param_hu.state_hu["pywardium"]["ip"]
    port = param_hu.state_hu["pywardium"]["http_server_port"]
    if(connected):
        try:
            sock = client.HTTPConnection(ip, port, timeout=1)
            sock.request("GET", "/state_py")
            response = sock.getresponse()
            data = response.read()
            parser_json.upload_file_by_sock_data(param_hu.path_state_py, data)
            param_hu.state_py = parser_json.load_file(param_hu.path_state_py)
            sock.close()
        except:
            http_client.connection_closed()
