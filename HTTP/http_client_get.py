#---------------------------------------------
# Possible GET command:
# - /test_http_conn
# - /py_state
#---------------------------------------------

from param import param_hu
from HTTP import http_client_fct
from src import parser_json

import json


def get_state(dest):
    [ip, port, connected] = http_client_fct.network_info(dest)
    command = "/" + dest + "_state"
    data = http_client_fct.send_http_get(ip, port, connected, command)
    if(data != None):
        parser_json.update_state_file(param_hu.path_state_py, data)
        param_hu.state_py = json.loads(data)

def send_command(dest, command):
    [ip, port, connected] = http_client_fct.network_info(dest)
    data = http_client_fct.send_http_get(ip, port, connected, command)
