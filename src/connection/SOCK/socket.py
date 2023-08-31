#---------------------------------------------
from src.param import param_edge
from src.connection.SOCK import socket_client
from src.connection.SOCK import socket_server


class Socket():
    def __init__(self):
        self.name = "Socket";
        self.init_sockets()

    def init_sockets(self):
        # Socket server lidar_1
        port = param_edge.state_edge["hub"]["socket"]["server_l1_port"]
        self.sock_server_l1 = socket_server.Socket_server("lidar_1", port, self.callback_l1_packet, self.callback_l1_deco)
        self.sock_server_l1.start_daemon()

        # Socket server lidar_2
        port = param_edge.state_edge["hub"]["socket"]["server_l2_port"]
        self.sock_server_l2 = socket_server.Socket_server("lidar_2", port, self.callback_l2_packet, self.callback_l2_deco)
        self.sock_server_l2.start_daemon()

        # Socket client
        self.sock_client = socket_client.Socket_client()

    def callback_l1_packet(self, packet):
        param_edge.state_edge["interface"]["capture"]["sock_l1_connected"] = True
        main_source = param_edge.state_edge["hub"]["socket"]["lidar_main"]
        if(main_source == "lidar_1"):
            self.sock_client.send_packet(packet, "control", "lidar_1")
            self.sock_client.send_packet(packet, "slam", "")
            if(param_edge.state_edge["slam"]["http"]["connected"]):
                param_edge.state_edge["slam"]["socket"]["connected"] = True
        elif(main_source == "lidar_2"):
            self.sock_client.send_packet(packet, "control", "lidar_2")
    def callback_l1_deco(self):
        param_edge.state_edge["interface"]["capture"]["sock_l1_connected"] = False
    def callback_l2_packet(self, packet):
        param_edge.state_edge["interface"]["capture"]["sock_l2_connected"] = True
        main_source = param_edge.state_edge["hub"]["socket"]["lidar_main"]
        if(main_source == "lidar_2"):
            self.sock_client.send_packet(packet, "control", "lidar_1")
            self.sock_client.send_packet(packet, "slam", "lidar_1")
            if(param_edge.state_edge["slam"]["http"]["connected"]):
                param_edge.state_edge["slam"]["socket"]["connected"] = True
        elif(main_source == "lidar_1"):
            self.sock_client.send_packet(packet, "control", "lidar_2")
    def callback_l2_deco(self):
        param_edge.state_edge["interface"]["capture"]["sock_l2_connected"] = False

    def stop_daemons(self):
        self.sock_server_l1.stop_daemon()
        self.sock_server_l2.stop_daemon()
