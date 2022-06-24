#! /usr/bin/python
#---------------------------------------------

from src import socket_config
import socket


def init_pywardium_hubium():
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.bind('', socket_config.port_pywar)
    socket.listen()
    return socket

def init_hubium_velodium():
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.connect((socket_config.ip_velo, socket_config.port_velo))
    return socket

def init_hubium_edge():
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.connect((socket_config.ip_edge, socket_config.port_edge))
    return socket

def init_edge_hubium():
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.bind('', socket_config.port_edge)
    socket.listen()
    return socket

def loop_lidar_transfer():
    while 1:
        pass
