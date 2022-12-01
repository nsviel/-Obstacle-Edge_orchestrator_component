#---------------------------------------------
from param import param_hu
from SOCK import sock_client_fct

import socket


def connection():
    param_hu.sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_hu.sock_client_ok = True

def send_packet_l1(packet):
    # Send packet to Controlium
    [ip, port] = sock_client_fct.network_info("co", "l1")
    packet = packet[42:]
    sock_client_fct.send_packet_add(ip, port, packet)
    print(ip)

    # Send packet to Velodium
    [ip, port] = sock_client_fct.network_info("ve", "")
    try:
        sock_client_fct.send_packet_add(ip, port, packet)
        param_hu.state_hu["velodium"]["sock_connected"] = True
    except:
        param_hu.state_hu["velodium"]["sock_connected"] = False

def send_packet_l2(packet):
    [ip, port] = sock_client_fct.network_info("co", "l2")
    packet = packet[42:]
    sock_client_fct.send_packet_add(ip, port, packet)

def reset_connnection():
    param_hu.state_hu["velodium"]["sock_connected"] = False
