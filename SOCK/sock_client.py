#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from SOCK import sock_client_fct


def connection():
    sock_client_fct.create_socket()

def send_packet_l1(packet):
    ip = param_hu.state_hu["controlium"]["ip"]
    port = param_hu.state_hu["controlium"]["sock_server_l1_port"]
    sock_client_fct.send_packet_add(ip, port, packet)

def send_packet_l2(packet):
    ip = param_hu.state_hu["controlium"]["ip"]
    port = param_hu.state_hu["controlium"]["sock_server_l2_port"]
    sock_client_fct.send_packet_add(ip, port, packet)

def test_velo_connection():
    sock_client_fct.test_velo_connection()
