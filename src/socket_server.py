#! /usr/bin/python
#---------------------------------------------

from param import cla

from threading import Thread

import socket


def start_daemon():
    thread_con = Thread(target = thread_socket_server)
    thread_con.start()

def thread_socket_server():
    cla.hubium.sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cla.hubium.sock_server.bind(("127.0.0.1", cla.hubium.sock_server_port))
    cla.hubium.sock_server.settimeout(1)
    cla.hubium.run_thread_socket = True

    while cla.hubium.run_thread_socket:
        try:
            data, (address, port) = cla.hubium.sock_server.recvfrom(4096)
            msg = data.decode('utf-8')
            print(msg)
            if(msg == "test"):
                cla.hubium.sock_server.sendto(str.encode("ok"), (cla.connec.py_ip, cla.connec.py_sock_server_port))
            if(msg == "ok"):
                cla.connec.velo_sock_connected = True
        except:
            a=1
        pass
    cla.hubium.sock_server.close()
