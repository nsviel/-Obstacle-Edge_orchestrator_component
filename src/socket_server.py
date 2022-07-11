#! /usr/bin/python
#---------------------------------------------

from param import cla

from threading import Thread

import socket


def start_thread_socket_server():
    thread_con = Thread(target = thread_socket_server)
    thread_con.start()

def thread_socket_server():
    cla.hubium.sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cla.hubium.sock_server.bind(("127.0.0.1", cla.hubium.sock_port_listen))
    cla.hubium.sock_server.settimeout(1)
    cla.hubium.run_thread_socket = True

    while cla.hubium.run_thread_socket:
        try:
            data, (address, port) = cla.hubium.sock_server.recvfrom(4096)
            msg = data.decode('utf-8')
            if(msg == "test"):
                cla.hubium.sock_server.sendto(str.encode("ok"), ("127.0.0.1", cla.connec.py_sock_port))
        except:
            a=1
        pass
    cla.hubium.sock_server.close()
