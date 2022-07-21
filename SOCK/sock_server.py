#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from SOCK import sock_server_fct

from threading import Thread


def start_daemon():
    thread_con = Thread(target = sock_server_fct.thread_socket_l1_server)
    thread_con.start()

def stop_daemon():
    param_hu.run_thread_socket = False
