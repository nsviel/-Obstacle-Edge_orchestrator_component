#---------------------------------------------
from src.connection import connection
from src.connection.SOCK import sock_server_l1
from src.connection.SOCK import sock_server_l2
from src.network import network_manager


class Daemons():
    def __init__(self):
        self.daemon_connection = connection.Connection()
        self.daemon_socket_l1 = sock_server_l1.Socket_l1()
        self.daemon_socket_l2 = sock_server_l2.Socket_l2()
        self.daemon_network = network_manager.Network()

    def start_daemons(self):
        self.daemon_connection.start_daemon()
        self.daemon_socket_l1.start_daemon()
        self.daemon_socket_l2.start_daemon()
        self.daemon_network.start_daemon()

    def stop_daemons(self):
        self.daemon_connection.stop_daemon()
        self.daemon_socket_l1.stop_daemon()
        self.daemon_socket_l2.stop_daemon()
        self.daemon_network.stop_daemon()
