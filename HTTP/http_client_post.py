#! /usr/bin/python
#---------------------------------------------
# Possible POST command:
# - /py_state
# - /py_param
# - /ve_param
# - /ai_param
#---------------------------------------------

from HTTP import http_client_fct

import json


def post_command(dest, command, value):
    [ip, port, connected] = http_client_fct.network_info(dest)
    http_client_fct.send_http_post(ip, port, connected, command, payload)

def post_param_payload(dest, payload):
    [ip, port, connected] = http_client_fct.network_info(dest)
    command = "/" + dest + "_param"
    http_client_fct.send_http_post(ip, port, connected, command, payload)

def post_param_value(dest, lvl1, lvl2, value):
    [ip, port, connected] = http_client_fct.network_info(dest)
    command = "/" + dest + "_param"
    payload = json.dumps({lvl1: {lvl2: value}})
    http_client_fct.send_http_post(ip, port, connected, command, payload)

def post_state(dest, state):
    [ip, port, connected] = http_client_fct.network_info(dest)
    command = "/" + dest + "_state"
    payload = json.dumps(state).encode(encoding='utf_8')
    http_client_fct.send_http_post(ip, port, connected, command, payload)
