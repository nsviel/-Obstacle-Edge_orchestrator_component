#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from HTTP import http_client
from HTTP import http_server_forward
from src import connection
from src import parser_json
from src import io

import http.client as client
import json


def post_param(self):
    content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
    post_data = self.rfile.read(content_length) # <--- Gets the data itself
    self.send_response(200)
    try:
        data = post_data.decode('utf8')
        return data
    except:
        print("[\033[1;31merror\033[0m] POST param failed")

def send_image(self, path):
    try:
        self.send_response(200)
        self.send_header("Content-type", "image/bmp")
        self.end_headers()
        if(os.path.isfile(path)):
            bin = io.load_binary(path)
            self.wfile.write(bin)
    except:
        print("[\033[1;31merror\033[0m] Image sending failed (\033[1;32m%s\033[0m)" % path)

def send_state(self, path):
    try:
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        data = parser_json.load_file_to_sock_data_encoded(path)
        self.wfile.write(data)
    except:
        print("[\033[1;31merror\033[0m] State sending failed")

def process_post_hu_param(self):
    content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
    post_data = self.rfile.read(content_length) # <--- Gets the data itself
    self.send_response(200)
    try:
        data = post_data.decode('utf8')
        data = json.loads(data)

        for key, value in data.items():
            lvl1 = key
            for key_, value_ in data[key].items():
                lvl2 = key_
                lvl3 = value_

        param_hu.state_hu[lvl1][lvl2] = lvl3
    except:
        print('[\033[1;31merror\033[0m] Processing post param failed')

def process_post_ve_param(self):
    content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
    post_data = self.rfile.read(content_length) # <--- Gets the data itself
    self.send_response(200)
    try:
        data = post_data.decode('utf8')
        data = json.loads(data)

        for key, value in data.items():
            lvl1 = key
            lvl2 = value

        http_server_forward.process_post_data(lvl1, lvl2)
    except:
        print('[\033[1;31merror\033[0m] Processing post param failed')

def process_post_ai_param(self):
    content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
    post_data = self.rfile.read(content_length) # <--- Gets the data itself
    self.send_response(200)
    try:
        data = post_data.decode('utf8')
        data = json.loads(data)

        for key, value in data.items():
            lvl1 = key
            lvl2 = value

        http_server_forward.forward_ve_post_data(lvl1, lvl2)
    except:
        print('[\033[1;31merror\033[0m] Processing post param failed')
