#---------------------------------------------
from src.param import param_edge
from src.connection.HTTPS.server import https_server
from src.connection.MQTT import mqtt_client
from src.connection.SOCK import sock_client
from src.connection import connection
from src.state import state
from src.utils import data
from src.utils import terminal
from src import daemon
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
    sock_client.create_socket()
    daemon.start_daemons()
    https_server.start_server()
    terminal.addLog("OK", "Program initialized...")
    terminal.addLine()

def loop():
    time.sleep(param_edge.tic_loop)

def end():
    terminal.shutdown()
    state.upload_states()
    daemon.stop_daemons()
    mqtt_client.mqtt_disconnection()
    https_server.stop_server()
    terminal.delai()
