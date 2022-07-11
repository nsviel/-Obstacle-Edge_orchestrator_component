#! /usr/bin/python
#---------------------------------------------

from param import classes

from threading import Thread

import socket


def start_thread_socket_server():
    thread_con = Thread(target = thread_socket_server)
    thread_con.start()

def thread_socket_server():
    classes.hubium.sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    classes.hubium.sock_server.bind(("127.0.0.1", classes.hubium.sock_port_listen))
    classes.hubium.sock_server.settimeout(1)
    classes.hubium.run_thread_socket = True

    while classes.hubium.run_thread_socket:
        try:
            data, (address, port) = classes.hubium.sock_server.recvfrom(4096)
            msg = data.decode('utf-8')
            if(msg == "test"):
                classes.hubium.sock_server.sendto(str.encode("ok"), ("127.0.0.1", classes.connec.py_sock_port))
        except:
            a=1
        pass
    classes.hubium.sock_server.close()
