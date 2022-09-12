#! /usr/bin/python
#---------------------------------------------

from param import param_hu

from HTTP import http_server_get
from HTTP import http_server_post

from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer

import threading
import http.server


class S(BaseHTTPRequestHandler):
    def do_GET(self):
        manage_get(self);

    def do_POST(self):
        manage_post(self);

    def log_message(self, format, *args):
        return

def manage_post(self):
    path = str(self.path)
    if(param_hu.http_server_verbose):
        print("---- POST request ----")
        print("Path: \033[94m%s\033[0m" % path)
        print("Headers:\n \033[94m%s\033[0m" % str(self.headers))
        print("Body:\n \033[94m%s\033[0m" % post_data.decode('utf-8'))
    if(path == '/geo'):
        http_server_post.post_geo(self)
    if(path == '/new_param_py'):
        http_server_post.post_param_py(self)
    if(path == '/new_param_hu'):
        http_server_post.post_param_hu(self)
    if(path == '/new_param_ve'):
        http_server_post.post_param_ve(self)
    if(path == '/new_param_ai'):
        http_server_post.post_param_ai(self)
    if(path == '/new_state_hu'):
        http_server_post.post_state_hu(self)
    if(path == '/new_state_py'):
        http_server_post.post_state_py(self)

def manage_get(self):
    path = str(self.path)
    if(param_hu.http_server_verbose):
        print("---- GET request ----")
        print("Path: \033[94m%s\033[0m" % path)
        print("Headers:\n \033[94m%s\033[0m" % str(self.headers))
        print("Body:\n \033[94m%s\033[0m" % post_data.decode('utf-8'))
    #Pywardium
    if(path == '/geo'):
        http_server_get.get_geo(self)
    elif(path == '/lidar_1_start'):
        http_server_get.get_lidar_1_start(self)
    elif(path == '/lidar_1_sttop'):
        http_server_get.get_lidar_1_stop(self)
    elif(path == '/lidar_2_start'):
        http_server_get.get_lidar_2_start(self)
    elif(path == '/lidar_2_stop'):
        http_server_get.get_lidar_2_stop(self)

    #Hubium
    elif(path == '/false_alarm'):
        http_server_get.get_false_alarm(self)
    elif(path == '/image'):
        http_server_get.get_image(self)
    elif(path == '/restart_sock_server'):
        http_server_get.get_restart_sock_server()
    elif(path == '/test_http_conn'):
        http_server_get.get_test_http_conn(self)
    elif(path == '/state_hu'):
        http_server_get.get_state_hu(self)
    elif(path == '/state_py'):
        http_server_get.get_state_py(self)

    #Velodium
    elif(path == '/state_py'):
        http_server_get.get_state_py(self)
