#---------------------------------------------
from param import param_hu

from HTTPS import https_server
from MQTT import mqtt_client
from SOCK import sock_server
from SOCK import sock_client
from perf import perf_server_network
from perf import perf_client_network

from src import connection
from src import state
from src import parser_json
from src import data
from src import terminal

import time


def start():
    # Init variables
    init()

    # Start main loop program
    while param_hu.run_loop:
        loop()

    # Join threads
    end()

def init():
    data.check_directories()
    state.load_configuration()
    sock_client.connection()
    connection.start_daemon()
    sock_server.start_daemon()
    https_server.start_daemon()
    perf_server_network.start_daemon()
    perf_client_network.start_daemon()
    terminal.addLog("OK", "Program initialized...")
    terminal.addLine()

def loop():
    time.sleep(1)

def end():
    terminal.shutdown()
    parser_json.upload_file(param_hu.path_state_hu, param_hu.state_hu)
    connection.stop_daemon()
    sock_server.stop_daemon()
    https_server.stop_daemon()
    perf_server_network.stop_daemon()
    perf_client_network.stop_daemon()
