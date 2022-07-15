#! /usr/bin/python
#---------------------------------------------

from param import param_hu

import socket


# Test velodium connection
def test_velo_connection():
    port = param_hu.state_hu["velodium"]["sock_server_port"]
    connected = param_hu.state_hu["velodium"]["connected"]
    if(connected == False):
        sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock_client.sendto(str.encode("200"), ("127.0.0.1", port))
