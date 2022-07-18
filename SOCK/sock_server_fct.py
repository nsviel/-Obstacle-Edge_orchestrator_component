#! /usr/bin/python
#---------------------------------------------

from param import param_hu

from threading import Thread

import socket


def thread_socket_server():
    port = param_hu.state_hu["self"]["sock_server_port"]
    ip = param_hu.state_hu["pywardium"]["ip"]

    param_hu.sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_hu.sock_server.bind(("127.0.0.1", port))
    param_hu.sock_server.settimeout(1)
    param_hu.run_thread_socket = True

    while param_hu.run_thread_socket:
        try:
            data, (address, port) = param_hu.sock_server.recvfrom(4096)
            process_data(data)
        except:
            pass

    param_hu.sock_server.close()

def process_data():
    msg = data.decode('utf-8')
    if(msg == "ok"):
        param_hu.state_hu["velodium"]["connected"] = True
