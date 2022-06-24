#! /usr/bin/python
#---------------------------------------------

from src import http_config
from src import write_data
from src import config
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
def run(server_class=HTTPServer, handler_class=S):
    server_address = (http_config.ip, http_config.port)
    server = ThreadingHTTPServer(server_address, handler_class)
    httpd = threading.Thread(target=server.serve_forever)
    httpd.daemon = True
    httpd.start()
    print('Starting httpd port ', http_config.port)

#Command functions
def manage_post(self):
    content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
    post_data = self.rfile.read(content_length) # <--- Gets the data itself
    path = str(self.path)

    if(http_config.verbose):
        print("---- POST request ----")
        print("Path: \033[94m%s\033[0m" % path)
        print("Headers:\n \033[94m%s\033[0m" % str(self.headers))
        print("Body:\n \033[94m%s\033[0m" % post_data.decode('utf-8'))
    if(path == '/geo'):
        write_data.write_data(config.path_geolocalization, post_data.decode('utf-8'))
    if(path == '/velodyne'):
        print("velodyne !")
    if(path == '/scala'):
        print("scala !")
def manage_get(self):
    path = str(self.path)

    if(http_config.verbose):
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
       self.wfile.write(load_binary(config.path_image))

#Specific functions
def load_binary(filename):
    with open(filename, 'rb') as file_handle:
        return file_handle.read()
