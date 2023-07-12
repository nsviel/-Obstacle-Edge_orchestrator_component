#---------------------------------------------
from src.param import param_edge

import socket


def send_packet_add(ip, port, packet):
    if(packet != None and param_edge.sock_client_ok):
        param_edge.sock_client.sendto(packet, (ip, port))

def network_info(dest, lidar):
    if(dest == "co"):
        ip = param_edge.state_edge["module_interface"]["ip"]
        if(lidar == "l1"):
            port = param_edge.state_edge["module_interface"]["sock_server_l1_port"]
        if(lidar == "l2"):
            port = param_edge.state_edge["module_interface"]["sock_server_l2_port"]
    elif(dest == "processing"):
        ip = param_edge.state_edge["component_process"]["ip"]
        port = param_edge.state_edge["component_process"]["sock_server_port"]

    return [ip, port]
