#! /usr/bin/python
#---------------------------------------------

from param import cla

import socket


# Test velodium connection
def test_connection():
    sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_server.bind(("127.0.0.1", cla.hubium.sock_port_connection))
    sock_server.settimeout(0.1)
    try:
        sock_client.sendto(str.encode("200"), (cla.connec.velo_ip, cla.connec.velo_port))
        data, (address, port) = sock_server.recvfrom(4096)
        msg = data.decode('utf-8')
        if(msg == "ok"):
            cla.connec.velo_connected = True
    except:
        cla.connec.velo_connected = False
