#---------------------------------------------
from src.param import param_edge
from src.connection.HTTPS import https_server
from src.connection.MQTT import mqtt_client
from src.connection.SOCK import sock_server_l1
from src.connection.SOCK import sock_server_l2
from src.connection.SOCK import sock_client
from src.network import network_manager
from src.connection import connection
from src.state import state
from src.utils import parser_json
from src.utils import data
from src.utils import terminal

import time


daemon_connection = connection.Connection()
daemon_socket_l1 = sock_server_l1.Socket_l1()
daemon_socket_l2 = sock_server_l2.Socket_l2()
daemon_network = network_manager.Network()

def start():
    # Init variables
    init()

    # Start main loop program
    while param_edge.run_loop:
        loop()

    # Join threads
    end()

def init():
    data.check_directories()
    state.load_configuration()
    sock_client.create_socket()
    daemon_connection.start_daemon()
    daemon_socket_l1.start_daemon()
    daemon_socket_l2.start_daemon()
    daemon_network.start_daemon()
    https_server.start_daemon()
    terminal.addLog("OK", "Program initialized...")
    terminal.addLine()

def loop():
    time.sleep(param_edge.tic_loop)

def end():
    terminal.shutdown()
    state.upload_states()
    daemon_connection.stop_daemon()
    daemon_socket_l1.stop_daemon()
    daemon_socket_l2.stop_daemon()
    daemon_network.stop_daemon()
    mqtt_client.mqtt_disconnection()
    https_server.stop_daemon()
    terminal.delai()
