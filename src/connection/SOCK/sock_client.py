#---------------------------------------------
from src.param import param_edge
from src.connection.SOCK import sock_client_fct

import socket


def create_socket():
    param_edge.sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_edge.sock_client_ok = True

def send_packet_l1(packet):
    # We retrieve only the data from the packet
    packet = packet[len(packet) - 1206:]

    # -> Send packet to module_interface
    [ip, port] = sock_client_fct.network_info("co", "l1")
    sock_client_fct.send_packet_add(ip, port, packet)

    # -> Send packet to Velodium
    [ip, port] = sock_client_fct.network_info("processing", "")
    try:
        sock_client_fct.send_packet_add(ip, port, packet)
    except:
        param_edge.state_edge_1["component_process"]["sock_connected"] = False

def send_packet_l2(packet):
    [ip, port] = sock_client_fct.network_info("co", "l2")

    # We retrieve only the data from the packet
    packet = packet[len(packet) - 1206:]

    sock_client_fct.send_packet_add(ip, port, packet)

def reset_connnection():
    param_edge.state_edge_1["component_process"]["sock_connected"] = False
