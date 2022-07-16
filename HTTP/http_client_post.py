#! /usr/bin/python
#---------------------------------------------

from param import param_hu

import http.client as client
import json


def post_param_py(payload):
    http_client_fct.send_param_request("/new_param_py", payload)
