#---------------------------------------------
from src.param import param_edge
from src.connection.SOCK import socket
import socket


class Socket_client():
    def __init__(self):
        self.socket = None
        self.create_socket()

    def create_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_packet(self, packet, dest, source):
        packet = packet[len(packet) - 1206:]
        [ip, port] = network_info(dest, source)
        if(packet != None):
            self.socket.sendto(packet, (ip, port))

def network_info(dest, source):
    if(dest == "control"):
        ip = param_edge.state_control["control"]["info"]["ip"]
        if(source == "lidar_1"):
            port = param_edge.state_control["control"]["socket"]["server_l1_port"]
        if(source == "lidar_2"):
            port = param_edge.state_control["control"]["socket"]["server_l2_port"]
    elif(dest == "slam"):
        ip = param_edge.state_edge["hub"]["info"]["ip"]
        port = param_edge.state_edge["slam"]["socket"]["server_port"]
    return [ip, port]
