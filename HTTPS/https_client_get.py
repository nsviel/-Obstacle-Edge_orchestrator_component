#---------------------------------------------
# Possible GET command:
# - /test_http_conn
# - /py_state
#---------------------------------------------

from param import param_hu
from HTTPS import https_client_fct
from src import parser_json

import json


def get_state(dest):
    [ip, port, connected] = https_client_fct.network_info(dest)
    command = "/" + dest + "_state"
    data = https_client_fct.send_https_get(ip, port, connected, command)

    if(data != None):
        if(dest == "py"):
            parser_json.update_state_file(param_hu.path_state_py, data)
            param_hu.state_py = json.loads(data)
        elif(dest == "perf"):
            parser_json.update_state_file(param_hu.path_state_perf, data)
            param_hu.state_perf = json.loads(data)

def send_command(dest, command):
    [ip, port, connected] = https_client_fct.network_info(dest)
    data = https_client_fct.send_https_get(ip, port, connected, command)
