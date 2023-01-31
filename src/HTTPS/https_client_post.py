#---------------------------------------------
# Possible POST command:
# - /py_state
# - /py_param
# - /ve_param
# - /ai_param
#---------------------------------------------

from src.HTTPS import https_client_fct

import json


def post_command(dest, command, value):
    [ip, port, connected] = https_client_fct.network_info(dest)
    https_client_fct.send_https_post(ip, port, connected, command, value)

def post_param_payload(dest, payload):
    [ip, port, connected] = https_client_fct.network_info(dest)
    command = "/" + dest + "_param"
    https_client_fct.send_https_post(ip, port, connected, command, payload)

def post_param_value(dest, lvl1, lvl2, value):
    [ip, port, connected] = https_client_fct.network_info(dest)
    command = "/" + dest + "_param"
    payload = json.dumps({lvl1: {lvl2: value}})
    https_client_fct.send_https_post(ip, port, connected, command, payload)

def post_state(dest, state):
    [ip, port, connected] = https_client_fct.network_info(dest)
    command = "/" + dest + "_state"
    payload = json.dumps(state).encode(encoding='utf_8')
    https_client_fct.send_https_post(ip, port, connected, command, payload)
