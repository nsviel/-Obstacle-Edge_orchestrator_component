#---------------------------------------------
from src.param import param_edge
from src.connection.HTTPS import https_server_get
from src.connection.HTTPS import https_server_post
from src.utils import terminal

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
    address = ("", param_edge.state_edge_1["self"]["http_server_port"])

    try:
        param_edge.https_server = http.server.ThreadingHTTPServer(address, handler_class)
        param_edge.http_server_daemon = threading.Thread(target=param_edge.https_server.serve_forever)
        param_edge.http_server_daemon.daemon = True
        param_edge.http_server_daemon.start()
        terminal.addDaemon("#", "ON", "HTTPS server")
    except:
        terminal.addLog("error", "HTTPS address already used")
        terminal.fatal_error()
        os.system("sudo kill -9 $(ps -A | grep python | awk '{print $1}')")

def stop_daemon():
    param_edge.https_server.shutdown()
    param_edge.http_server_daemon.join()
    terminal.addDaemon("#", "OFF", "HTTPS server")
