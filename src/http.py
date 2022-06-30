#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import io
from src import mqtt
from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer

import threading
import http.server
import io


#Server functions
class S(BaseHTTPRequestHandler):
    def log(self):
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_GET(self):
        manage_get(self);
        self.log()

    def do_POST(self):
        manage_post(self);
        self.log()

def connect(server_class=HTTPServer, handler_class=S):
    server_address = (parameter.http_ip, parameter.http_port)
    server = ThreadingHTTPServer(server_address, handler_class)
    httpd = threading.Thread(target=server.serve_forever)
    httpd.daemon = True
    httpd.start()
    parameter.http_is_connected = True

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
        print("geo !")
    if(path == '/image'):
       self.send_response(200)
       self.send_header("Content-type", "image/bmp")
       self.end_headers()
       self.wfile.write(load_binary(parameter.path_image))
    if(path == '/falsealarm'):
       mqtt.publish_false_alarm()
    if(path == '/test'):
       self.send_response(200)

#Specific functions
def load_binary(filename):
    with open(filename, 'rb') as file_handle:
        return file_handle.read()
