#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from conn import http_client_post
from src import parser_json
from src import io

import json


def post_geo():
    io.write_data(param_hu.path_geoloc, post_data.decode('utf-8'))

def post_new_state_py(self):
    content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
    post_data = self.rfile.read(content_length) # <--- Gets the data itself
    self.send_response(200)
    try:
        data = post_data.decode('utf8')
        data = json.loads(data)
        param_hu.state_py = data
        parser_json.upload_file(param_hu.path_state_py, param_hu.state_py)
        http_client_post.post_new_state_py()
    except:
        print('not valid JSON')

def post_new_param_py(self):
    content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
    post_data = self.rfile.read(content_length) # <--- Gets the data itself
    self.send_response(200)
    try:
        data = post_data.decode('utf8')
        http_client_post.post_new_param_py(data)
    except:
        print('not valid JSON')
