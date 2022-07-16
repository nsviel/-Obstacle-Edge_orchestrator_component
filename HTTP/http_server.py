#! /usr/bin/python
#---------------------------------------------

from param import param_hu

from HTTP import http_server_get
from HTTP import http_server_post
from HTTP import http_server_class

from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer

import threading
import http.server


def start_daemon(server_class=HTTPServer, handler_class=http_server_class.S):
    address = ("", param_hu.state_hu["self"]["http_server_port"])
    param_hu.http_server = ThreadingHTTPServer(address, handler_class)
    param_hu.http_server_daemon = threading.Thread(target=param_hu.http_server.serve_forever)
    param_hu.http_server_daemon.daemon = True
    param_hu.http_server_daemon.start()

def stop_daemon():
    param_hu.http_server.shutdown()
    param_hu.http_server_daemon.join()
