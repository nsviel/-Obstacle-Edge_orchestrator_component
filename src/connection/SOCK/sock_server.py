#---------------------------------------------
from src.param import param_edge
from src.connection.SOCK import sock_server_fct
from src.connection import connection
from src.utils import terminal

import threading
import time


def start_daemon():
    thread_l1 = threading.Thread(target = sock_server_fct.thread_socket_l1_server)
    thread_l2 = threading.Thread(target = sock_server_fct.thread_socket_l2_server)
    thread_l1.start()
    thread_l2.start()
    terminal.addDaemon("#", "ON", "Socket server")

def stop_daemon():
    param_edge.run_thread_socket = False
    terminal.addDaemon("#", "OFF", "Socket server")

def restart_daemon():
    terminal.addDaemon("#", "restart", "Socket server")
    stop_daemon()
    time.sleep(1)
    start_daemon()

def check_port():
    l1_port = param_edge.state_edge["self"]["sock_server_l1_port"]
    l2_port = param_edge.state_edge["self"]["sock_server_l2_port"]
    connection.check_port_open(l1_port)
    connection.check_port_open(l2_port)
    if(l1_port == l2_port):
        print("[\033[1;31merror\033[0m] Problem attribution port [%s]" % (l1_port))
        return False
    return True
