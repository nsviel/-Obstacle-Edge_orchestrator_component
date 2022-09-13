#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from HTTP import http_client_post
from HTTP import http_client_get
from HTTP import http_server_fct
from src import parser_json
from src import io

import json


def post_geo():
    io.write_data(param_hu.path_geoloc, post_data.decode('utf-8'))
def post_param_py(self):
    data = http_server_fct.post_param(self)
    http_client_post.post_param_py(data)
    http_client_get.get_state_py()
def post_param_hu(self):
    self.send_response(200)
    try:
        data = http_server_fct.decode_post_json(self)
        for key, value in data.items():
            lvl1 = key
            for key_, value_ in data[key].items():
                lvl2 = key_
                lvl3 = value_
        param_hu.state_hu[lvl1][lvl2] = lvl3
        if(lvl1 == "sncf"):
            param_hu.state_hu["sncf"]["broker_connected"] = False
    except:
        print('[\033[1;31merror\033[0m] Processing post param failed')
def post_param_ve(self):
    self.send_response(200)
    try:
        data = http_server_fct.decode_post_json(self)
        for key, value in data.items():
            lvl1 = key
            lvl2 = value
        http_server_forward.process_post_data(lvl1, lvl2)
    except:
        print('[\033[1;31merror\033[0m] Processing post param failed')
def post_param_ai(self):
    self.send_response(200)
    try:
        data = http_server_fct.decode_post_json(self)
        for key, value in data.items():
            lvl1 = key
            lvl2 = value
        http_server_forward.forward_ve_post_data(lvl1, lvl2)
    except:
        print('[\033[1;31merror\033[0m] Processing post param failed')


def post_state_hu(self):
    self.send_response(200)
    try:
        data = http_server_fct.decode_post_json(self)
        param_hu.state_hu = data
        parser_json.upload_state()
        param_hu.state_hu["sncf"]["status"] = "Offline"
        param_hu.state_hu["sncf"]["broker_connected"] = False
    except:
        print('[\033[1;31merror\033[0m] Processing post param failed')

def post_state_py(self):
    self.send_response(200)
    try:
        data = http_server_fct.decode_post_json(self)
        http_client_post.send_py_state(data)
    except:
        print('[\033[1;31merror\033[0m] Processing post param failed')
