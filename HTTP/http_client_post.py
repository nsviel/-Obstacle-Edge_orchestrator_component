#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from HTTP import http_client_fct

import http.client as client
import json


def post_param_py(payload):
    if(param_hu.state_hu["pywardium"]["http_connected"]):
        http_client_fct.send_post_request_py("/new_param_py", payload)

def post_param_ve(payload):
    if(param_hu.state_hu["velodium"]["http_connected"]):
        http_client_fct.send_post_request_ve("/new_param_py", payload)
