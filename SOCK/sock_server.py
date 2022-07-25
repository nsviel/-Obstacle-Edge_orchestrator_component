#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from SOCK import sock_server_fct

from threading import Thread


def start_daemon():
    thread_l1 = Thread(target = sock_server_fct.thread_socket_l1_server)
    thread_l2 = Thread(target = sock_server_fct.thread_socket_l2_server)
    thread_l1.start()
    thread_l2.start()

def stop_daemon():
    param_hu.run_thread_socket = False
