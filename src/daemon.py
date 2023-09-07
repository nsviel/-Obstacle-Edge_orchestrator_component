#---------------------------------------------
from src.connection import connection
from src.connection.SOCK import socket
from src.network import network


class Daemons():
    def __init__(self):
        self.daemon_connection = connection.Connection()
        self.daemon_socket = socket.Socket()
        self.daemon_network = network.Network()

    def start_daemons(self):
        self.daemon_connection.start_daemon()
        self.daemon_network.start_daemon()

    def stop_daemons(self):
        self.daemon_connection.stop_daemon()
        self.daemon_socket.stop_daemons()
        self.daemon_network.stop_daemon()
