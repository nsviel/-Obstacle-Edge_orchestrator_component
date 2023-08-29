#---------------------------------------------
# Possible GET command:
# - /test_http_conn
# - /capture_state
#---------------------------------------------

from src.param import param_edge
from src.connection.HTTPS.client import https_client_fct
from src.utils import parser_json

import json


def get_state(dest):
    [ip, port, connected] = https_client_fct.network_info(dest)
    command = "/" + dest + "_state"
    data = https_client_fct.send_https_get(ip, port, connected, command)

    if(data != None):
        try:
            if(dest == "capture"):
                parser_json.update_state_file(param_edge.path_state_ground, data)
                param_edge.state_ground = json.loads(data)
            elif(dest == "network"):
                param_edge.state_network = json.loads(data)
        except:
            print("[\033[1;31merror\033[0m] GET \033[1;32m%s\033[0m state failed"% dest)

def get_state_data(dest):
    [ip, port, connected] = https_client_fct.network_info(dest)
    command = "/" + dest + "_state"
    data = https_client_fct.send_https_get(ip, port, connected, command)

    if(data != None):
        try:
            if(dest == "capture"):
                parser_json.update_state_file(param_edge.path_state_ground, data)
                return json.loads(data)
            elif(dest == "network"):
                return json.loads(data)
        except:
            print("[\033[1;31merror\033[0m] GET \033[1;32m%s\033[0m state failed"% dest)

def send_command(dest, command):
    [ip, port, connected] = https_client_fct.network_info(dest)
    data = https_client_fct.send_https_get(ip, port, connected, command)
    return data
