#---------------------------------------------
from param import param_hu
from HTTPS import https_server_get
from HTTPS import https_server_post

import http.server
import threading
import os


class S(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        https_server_get.manage_get(self);

    def do_POST(self):
        https_server_post.manage_post(self);

    def log_message(self, format, *args):
        return

def start_daemon(server_class=http.server.HTTPServer, handler_class=S):
    address = ("", param_hu.state_hu["self"]["http_server_port"])

    try:
        param_hu.https_server = http.server.ThreadingHTTPServer(address, handler_class)
        param_hu.http_server_daemon = threading.Thread(target=param_hu.https_server.serve_forever)
        param_hu.http_server_daemon.daemon = True
        param_hu.http_server_daemon.start()
    except:
        print("[\033[1;31merror\033[0m] Address already in use")
        os.system("sudo kill -9 $(ps -A | grep python | awk '{print $1}')")

def stop_daemon():
    param_hu.https_server.shutdown()
    param_hu.http_server_daemon.join()
