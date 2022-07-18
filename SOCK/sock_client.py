#! /usr/bin/python
#---------------------------------------------

from SOCK import sock_client_fct


def connection():
    sock_client_fct.create_socket()

def send_packet(packet):
    ip = param_hu.state_py["hubium"]["ip"]
    port = param_hu.state_py["hubium"]["sock_server_port"]
    send_packet_add(ip, port, packet)

def test_velo_connection():
    sock_client_fct.test_velo_connection()
