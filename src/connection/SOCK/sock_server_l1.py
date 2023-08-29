#---------------------------------------------
from src.param import param_edge
from src.utils import terminal
from src.base import daemon
from src.connection.SOCK import sock_client

import socket


class Socket_l1(daemon.Daemon):
    def thread_init(self):
        port = param_edge.state_edge["hub"]["socket"]["server_l1_port"]
        param_edge.sock_server_l1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        param_edge.sock_server_l1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        param_edge.sock_server_l1.bind(("", port))
        param_edge.sock_server_l1.settimeout(1)

    def thread_function(self):
        try:
            data, (address, port) = param_edge.sock_server_l1.recvfrom(4096)
            param_edge.state_ground["capture"]["socket"]["l1_connected"] = True
            process_data(data)
        except:
            param_edge.state_ground["capture"]["socket"]["l1_connected"] = False

    def process_data(data):
        if(param_edge.state_edge["hub"]["lidar_main"] == "lidar_1"):
            sock_client.send_packet_l1(data)
        elif(param_edge.state_edge["hub"]["lidar_main"] == "lidar_2"):
            sock_client.send_packet_l2(data)

    def thread_end(self):
        param_edge.sock_server_l1.close()

    name = "Socket server LiDAR 1";
    run_sleep = 0;
