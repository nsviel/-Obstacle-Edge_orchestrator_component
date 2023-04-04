#---------------------------------------------
from src.param import param_edge
from src.HTTPS import https_server
from src.MQTT import mqtt_client
from src.SOCK import sock_server
from src.SOCK import sock_client
from src.network import perf_network
from src.misc import connection
from src.misc import state
from src.misc import parser_json
from src.misc import data
from src.misc import terminal

import time


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
    sock_client.connection()
    connection.start_daemon()
    sock_server.start_daemon()
    https_server.start_daemon()
    perf_network.start_daemon()
    terminal.addLog("OK", "Program initialized...")
    terminal.addLine()

def loop():
    time.sleep(param_edge.tic_loop)

def end():
    terminal.shutdown()
    parser_json.upload_file(param_edge.path_state_edge, param_edge.state_edge)
    connection.stop_daemon()
    sock_server.stop_daemon()
    https_server.stop_daemon()
    perf_network.stop_daemon()
    terminal.delai()
