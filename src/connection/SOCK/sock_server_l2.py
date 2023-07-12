#---------------------------------------------
from src.param import param_edge
from src.utils import terminal
from src.utils import daemon
from src.connection.SOCK import sock_client

import socket


class Socket_l2(daemon.Daemon):
    def thread_init(self):
        port = param_edge.state_edge_1["self"]["sock_server_l2_port"]
        param_edge.sock_server_l2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        param_edge.sock_server_l2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        param_edge.sock_server_l2.bind(("", port))
        param_edge.sock_server_l2.settimeout(1)

    def thread_function(self):
        try:
            data, (address, port) = param_edge.sock_server_l2.recvfrom(1500)
            param_edge.state_edge_1["module_capture"]["sock_l2_connected"] = True
            process_data(data)
        except:
            param_edge.state_edge_1["module_capture"]["sock_l2_connected"] = False

    def process_data(data):
        if(param_edge.state_edge_1["self"]["lidar_main"] == "lidar_2"):
            sock_client.send_packet_l1(data)
        elif(param_edge.state_edge_1["self"]["lidar_main"] == "lidar_1"):
            sock_client.send_packet_l2(data)

    def thread_end(self):
        param_edge.sock_server_l2.close()

    name = "Socket server LiDAR 2";
    run_sleep = 0;
