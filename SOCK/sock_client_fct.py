#! /usr/bin/python
#---------------------------------------------

from param import param_hu

import socket


def create_socket():
    param_hu.sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_hu.sock_client_ok = True

def send_packet(packet):
    ip = param_hu.state_py["hubium"]["ip"]
    port = param_hu.state_py["hubium"]["sock_server_l1_port"]
    if(packet != None and param_hu.sock_client_ok):
        #Remove network queue data
        packet = packet[42:]

        #Send raw data
        param_hu.sock_client.sendto(packet, (ip, port))

def send_packet_add(ip, port, packet):
    if(packet != None and param_hu.sock_client_ok):
        #Remove network queue data
        packet = packet[42:]

        #Send raw data
        param_hu.sock_client.sendto(packet, (ip, port))

def test_velo_connection():
    port = param_hu.state_hu["velodium"]["sock_server_port"]
    if(param_hu.sock_client_ok):
        param_hu.sock_client.sendto(str.encode("200"), ("127.0.0.1", port))
