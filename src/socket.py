#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from param import param_ext

import socket


def test_connection():
    print("loop on %d" % param_ext.velo_port)
    sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_server.bind(("127.0.0.1", param_hu.sock_port_listen))
    sock_server.settimeout(0.1)
    try:
        sock_client.sendto(str.encode("200"), (param_ext.velo_ip, param_ext.velo_port))
        data, (address, port) = sock_server.recvfrom(4096)
        msg = data.decode('utf-8')
        print(msg)
        if(msg == "ok"):
            param_ext.velo_connected = True
    except:
        param_ext.velo_connected = False
