#! /usr/bin/python
#---------------------------------------------

from param import param_hu

from conn import http_server_get
from conn import http_server_post

from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer

import threading
import http.server


#Server functions
class S(BaseHTTPRequestHandler):
    def do_GET(self):
        manage_get(self);

    def do_POST(self):
        manage_post(self);

    def log_message(self, format, *args):
        return

def start_daemon(server_class=HTTPServer, handler_class=S):
    address = ("", param_hu.state_hu["self"]["http_server_port"])
    param_hu.http_server = ThreadingHTTPServer(address, handler_class)
    param_hu.http_server_daemon = threading.Thread(target=param_hu.http_server.serve_forever)
    param_hu.http_server_daemon.daemon = True
    param_hu.http_server_daemon.start()

def stop_daemon():
    param_hu.http_server.shutdown()
    param_hu.http_server_daemon.join()

#Command functions
def manage_post(self):
    path = str(self.path)

    if(param_hu.http_server_verbose):
        print("---- POST request ----")
        print("Path: \033[94m%s\033[0m" % path)
        print("Headers:\n \033[94m%s\033[0m" % str(self.headers))
        print("Body:\n \033[94m%s\033[0m" % post_data.decode('utf-8'))
    if(path == '/geo'):
        http_server_post.post_geo(self)
    if(path == '/new_state_py'):
        http_server_post.post_new_state_py(self)
    if(path == '/new_param_py'):
        http_server_post.post_new_param_py(self)

def manage_get(self):
    path = str(self.path)
    if(param_hu.http_server_verbose):
        print("---- GET request ----")
        print("Path: \033[94m%s\033[0m" % path)
        print("Headers:\n \033[94m%s\033[0m" % str(self.headers))
        print("Body:\n \033[94m%s\033[0m" % post_data.decode('utf-8'))
    if(path == '/geo'):
        http_server_get.get_geo(self)
    elif(path == '/image'):
       http_server_get.get_image(self)
    elif(path == '/falsealarm'):
       http_server_get.get_falsealarm(self)
    elif(path == '/test_http_conn'):
       http_server_get.get_test_http_conn(self)
    elif(path == '/state_hu'):
        http_server_get.get_state_hu(self)
    elif(path == '/state_py'):
         http_server_get.get_state_py(self)
