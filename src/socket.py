#! /usr/bin/python
#---------------------------------------------

from param import classes

import socket


# Test velodium connection
def test_connection():
    sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_server.bind(("127.0.0.1", classes.hubium.sock_port_connection))
    sock_server.settimeout(0.1)
    try:
        sock_client.sendto(str.encode("200"), (classes.connec.velo_ip, classes.connec.velo_port))
        data, (address, port) = sock_server.recvfrom(4096)
        msg = data.decode('utf-8')
        if(msg == "ok"):
            classes.connec.velo_connected = True
    except:
        classes.connec.velo_connected = False
