#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from HTTP import http_client
from HTTP import http_client_fct
from src import parser_json

import http.client as client
import requests


def get_state_py():
    state = http_client_fct.send_get_state("/state_py")
    if(state != None):
        parser_json.upload_file_by_sock_data(param_hu.path_state_py, state)
        param_hu.state_py = parser_json.load_file(param_hu.path_state_py)

def get_command(command, text):
    http_client_fct.send_get_command(command, text)
