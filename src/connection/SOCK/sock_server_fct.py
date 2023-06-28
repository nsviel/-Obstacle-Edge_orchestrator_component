#---------------------------------------------
from src.connection.SOCK import sock_client
from src.param import param_edge

import socket


def thread_socket_l1_server():
    port = param_edge.state_edge["self"]["sock_server_l1_port"]
    param_edge.sock_server_l1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_edge.sock_server_l1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    param_edge.sock_server_l1.bind(("", port))
    param_edge.sock_server_l1.settimeout(1)
    param_edge.run_thread_socket = True

    while param_edge.run_thread_socket:
        try:
            data, (address, port) = param_edge.sock_server_l1.recvfrom(4096)
            param_edge.state_edge["module_capture"]["sock_l1_connected"] = True
            process_l1_data(data)
        except:
            param_edge.state_edge["module_capture"]["sock_l1_connected"] = False

    param_edge.sock_server_l1.close()

def thread_socket_l2_server():
    port = param_edge.state_edge["self"]["sock_server_l2_port"]
    param_edge.sock_server_l2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_edge.sock_server_l2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    param_edge.sock_server_l2.bind(("", port))
    param_edge.sock_server_l2.settimeout(1)
    param_edge.run_thread_socket = True

    while param_edge.run_thread_socket:
        try:
            data, (address, port) = param_edge.sock_server_l2.recvfrom(1500)
            param_edge.state_edge["module_capture"]["sock_l2_connected"] = True
            process_l2_data(data)
        except:
            param_edge.state_edge["module_capture"]["sock_l2_connected"] = False

    param_edge.sock_server_l2.close()

def process_l1_data(data):
    if(param_edge.state_edge["self"]["lidar_main"] == "lidar_1"):
        sock_client.send_packet_l1(data)
    elif(param_edge.state_edge["self"]["lidar_main"] == "lidar_2"):
        sock_client.send_packet_l2(data)

def process_l2_data(data):
    if(param_edge.state_edge["self"]["lidar_main"] == "lidar_2"):
        sock_client.send_packet_l1(data)
    elif(param_edge.state_edge["self"]["lidar_main"] == "lidar_1"):
        sock_client.send_packet_l2(data)
