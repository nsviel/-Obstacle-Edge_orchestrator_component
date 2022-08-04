#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from SOCK import sock_server_fct

from threading import Thread
import time


def start_daemon():
    if(check_port_distribution()):
        thread_l1 = Thread(target = sock_server_fct.thread_socket_l1_server)
        thread_l2 = Thread(target = sock_server_fct.thread_socket_l2_server)
        thread_l1.start()
        thread_l2.start()

def stop_daemon():
    param_hu.run_thread_socket = False

def restart_daemon():
    print("[\033[1;32mOK\033[0m] Restart socket server daemon")
    stop_daemon()
    time.sleep(1)
    start_daemon()

def check_port_distribution():
    l1_port = param_hu.state_hu["self"]["sock_server_l1_port"]
    l2_port = param_hu.state_hu["self"]["sock_server_l2_port"]
    if(l1_port == l2_port):
        print("[\033[1;31merror\033[0m] Problem attribution port [%s]" % (l1_port))
        return False
    return True
