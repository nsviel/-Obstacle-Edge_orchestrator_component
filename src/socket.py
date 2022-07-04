#! /usr/bin/python
#---------------------------------------------

from src import parameter
import socket


def init_pywardium_hubium():
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.bind('', parameter.port_py_sock)
    socket.listen()
    return socket

def init_hubium_velodium():
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.connect((parameter.velo_ip, parameter.velo_port))
    return socket

def init_hubium_edge():
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.connect((parameter.ip_edge, parameter.port_edge))
    return socket

def init_edge_hubium():
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.bind('', parameter.port_edge)
    socket.listen()
    return socket

def loop_lidar_transfer():
    while 1:
        pass
