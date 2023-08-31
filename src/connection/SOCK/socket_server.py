#---------------------------------------------
from src.base import daemon
import socket


class Socket_server(daemon.Daemon):
    def __init__(self, name, port, callback_packet, callback_deco):
        self.name = "Socket server " + name;
        self.run_sleep = 0;
        self.socket = None
        self.port = port
        self.callback_packet = callback_packet
        self.callback_deco = callback_deco

    def thread_init(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(("", self.port))
        self.socket.settimeout(1)

    def thread_function(self):
        try:
            packet, (address, port) = self.socket.recvfrom(1500)
            self.callback_packet(packet)
        except:
            self.callback_deco

    def thread_end(self):
        self.socket.close()
