#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from HTTP import http_client_post
from HTTP import http_server_fct
from src import parser_json
from src import io

import json


def post_geo():
    io.write_data(param_hu.path_geoloc, post_data.decode('utf-8'))

def post_param_py(self):
    data = http_server_fct.post_param(self)
    http_client_post.post_param_py(data)

def post_param_hu(self):
    http_server_fct.process_post_param(self)

def post_param_ve(self):
    data = http_server_fct.post_param(self)
    http_client_post.post_param_ve(data)
