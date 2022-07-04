#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import io
from src import mqtt
from src import http_get

from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer

import threading
import http.server
import io


#Server functions
class S(BaseHTTPRequestHandler):
    def do_GET(self):
        manage_get(self);

    def do_POST(self):
        manage_post(self);

    def log_message(self, format, *args):
        return

def start_http_daemon(server_class=HTTPServer, handler_class=S):
    address = (parameter.http_ip, parameter.http_port)
    server = ThreadingHTTPServer(address, handler_class)
    httpd = threading.Thread(target=server.serve_forever)
    httpd.daemon = True
    httpd.start()

#Command functions
def manage_post(self):
    content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
    post_data = self.rfile.read(content_length) # <--- Gets the data itself
    path = str(self.path)

    if(parameter.http_verbose):
        print("---- POST request ----")
        print("Path: \033[94m%s\033[0m" % path)
        print("Headers:\n \033[94m%s\033[0m" % str(self.headers))
        print("Body:\n \033[94m%s\033[0m" % post_data.decode('utf-8'))
    if(path == '/geo'):
        io.write_data(parameter.path_geolocalization, post_data.decode('utf-8'))
    if(path == '/velodyne'):
        print("velodyne !")
    if(path == '/scala'):
        print("scala !")

def manage_get(self):
    path = str(self.path)

    if(parameter.http_verbose):
        print("---- GET request ----")
        print("Path: \033[94m%s\033[0m" % path)
        print("Headers:\n \033[94m%s\033[0m" % str(self.headers))
        print("Body:\n \033[94m%s\033[0m" % post_data.decode('utf-8'))
    if(path == '/geo'):
        http_get.get_geo(self)
    elif(path == '/image'):
       http_get.get_image(self)
    elif(path == '/falsealarm'):
       http_get.get_falsealarm(self)
    elif(path == '/test'):
       http_get.get_test(self)
    elif(path == '/state'):
        http_get.get_state(self)

#Specific functions
def load_binary(filename):
    with open(filename, 'rb') as file_handle:
        return file_handle.read()
