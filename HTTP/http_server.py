#---------------------------------------------
from param import param_hu
from HTTP import http_server_get
from HTTP import http_server_post

from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer
import threading


class S(BaseHTTPRequestHandler):
    def do_GET(self):
        http_server_get.manage_get(self);

    def do_POST(self):
        http_server_post.manage_post(self);

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
