#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from param import param_ext

from threading import Thread

import socket


def start_thread_socket_server():
    param_hu.sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_hu.sock_server.bind(("127.0.0.1", param_hu.sock_port))
    param_hu.sock_server.settimeout(1)
    param_hu.run_thread_socket = True
    thread_con = Thread(target = thread_socket_server)
    thread_con.start()

def thread_socket_server():
    while param_hu.run_thread_socket:
        try:
            print("wait data")
            data, (address, port) = param_hu.sock_server.recvfrom(4096)
            msg = data.decode('utf-8')
            print(msg)
            if(msg == "test"):
                param_hu.sock_server.sendto(str.encode("ok"), ("127.0.0.1", param_ext.py_sock_port))
        except:
            a=1
        pass
    param_hu.sock_server.close()
