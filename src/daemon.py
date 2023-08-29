#---------------------------------------------
from src.connection import connection
from src.connection.SOCK import sock_server_l1
from src.connection.SOCK import sock_server_l2
from src.network import network_manager


daemon_connection = connection.Connection()
daemon_socket_l1 = sock_server_l1.Socket_l1()
daemon_socket_l2 = sock_server_l2.Socket_l2()
daemon_network = network_manager.Network()

def start_daemons():
    daemon_connection.start_daemon()
    daemon_socket_l1.start_daemon()
    daemon_socket_l2.start_daemon()
    daemon_network.start_daemon()

def stop_daemons():
    daemon_connection.stop_daemon()
    daemon_socket_l1.stop_daemon()
    daemon_socket_l2.stop_daemon()
    daemon_network.stop_daemon()
