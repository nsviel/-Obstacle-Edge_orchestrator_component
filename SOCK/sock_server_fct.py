#! /usr/bin/python
#---------------------------------------------

from SOCK import sock_client
from param import param_hu

from threading import Thread

import socket


def thread_socket_l1_server():
    port = param_hu.state_hu["self"]["sock_server_l1_port"]
    ip = param_hu.state_hu["pywardium"]["ip"]

    param_hu.sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_hu.sock_server.bind(("127.0.0.1", port))
    param_hu.sock_server.settimeout(1)
    param_hu.run_thread_socket = True

    while param_hu.run_thread_socket:
        try:
            data, (address, port) = param_hu.sock_server.recvfrom(4096)
            param_hu.state_hu["pywardium"]["sock_l1_connected"] = True
            process_data(data)
        except:
            param_hu.state_hu["pywardium"]["sock_l1_connected"] = False

    param_hu.sock_server.close()

def thread_socket_l2_server():
    port = param_hu.state_hu["self"]["sock_server_l1_port"]
    ip = param_hu.state_hu["pywardium"]["ip"]

    param_hu.sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_hu.sock_server.bind(("127.0.0.1", port))
    param_hu.sock_server.settimeout(1)
    param_hu.run_thread_socket = True

    while param_hu.run_thread_socket:
        try:
            data, (address, port) = param_hu.sock_server.recvfrom(4096)
            param_hu.state_hu["pywardium"]["sock_l2_connected"] = True
            process_data(data)
        except:
            param_hu.state_hu["pywardium"]["sock_l2_connected"] = False

    param_hu.sock_server.close()

def process_data(data):
    msg = 0
    try:
        msg = data.decode('utf-8')
    except:
        pass
    if(msg == "ok"):
        param_hu.state_hu["velodium"]["sock_connected"] = True
    else:
        sock_client.send_packet(data)
