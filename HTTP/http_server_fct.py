#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from HTTP import http_client
from SOCK import sock_server
from src import connection
from src import parser_json

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
        print('not valid JSON')

def send_image(self, path):
    try:
        self.send_response(200)
        self.send_header("Content-type", "image/bmp")
        self.end_headers()
        if(os.path.isfile(path)):
            self.wfile.write(io.load_binary(path))
    except:
        pass

def send_state(self, path):
    try:
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        data = parser_json.load_file_to_sock_data_encoded(path)
        self.wfile.write(data)
    except:
        pass

def process_post_param(self):
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
        if(lvl1 == "self" and lvl2 == "sock_server_l1_port"):
            sock_server.restart_daemon()
        if(lvl1 == "self" and lvl2 == "sock_server_l2_port"):
            sock_server.restart_daemon()

    except:
        print('[\033[1;31merror\033[0m] Processing post param failed')
