#! /usr/bin/python
#---------------------------------------------

from HTTP import http_client_fct

import json


def post_command(dest, value):
    [ip, port, connected] = http_client_fct.network_info(dest)
    command = "/" + dest + "_command"
    http_client_fct.send_http_post(ip, port, connected, command, value)

def post_command_val(dest, lvl1, value):
    [ip, port, connected] = http_client_fct.network_info(dest)
    command = "/" + dest + "_command"
    payload = json.dumps({lvl1: value})
    http_client_fct.send_http_post(ip, port, connected, command, payload)

def post_param(dest, lvl1, value):
    [ip, port, connected] = http_client_fct.network_info(dest)
    command = "/" + dest + "_param"
    payload = json.dumps({lvl1: value})
    http_client_fct.send_http_post(ip, port, connected, command, payload)

def post_param_val(dest, lvl1, lvl2, value):
    [ip, port, connected] = http_client_fct.network_info(dest)
    command = "/" + dest + "_param"
    payload = json.dumps({lvl1: {lvl2: value}})
    http_client_fct.send_http_post(ip, port, connected, command, payload)

def post_param_payload(dest, payload):
    [ip, port, connected] = http_client_fct.network_info(dest)
    command = "/" + dest + "_param"
    http_client_fct.send_http_post(ip, port, connected, command, payload)

def post_state(dest, state):
    [ip, port, connected] = http_client_fct.network_info(dest)
    command = "/" + dest + "_state"
    payload = json.dumps(state).encode(encoding='utf_8')
    http_client_fct.send_http_post(ip, port, connected, command, payload)
