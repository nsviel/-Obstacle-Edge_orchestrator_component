#---------------------------------------------
from param import param_hu

from HTTP import http_server
from MQTT import mqtt_client
from SOCK import sock_server
from SOCK import sock_client

from src import connection
from src import state
from src import parser_json
from src import data
#from src import perf_server

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
    mqtt_client.create_client()
    sock_client.connection()
    connection.start_daemon()
    #perf_server.start_daemon()
    sock_server.start_daemon()
    http_server.start_daemon()

    param_hu.state_py["self"]["status"] = "Offline"
    param_hu.state_hu["edge"]["status"] = "Offline"
    param_hu.state_hu["self"]["status"] = "Online"
    print("[\033[1;32mOK\033[0m] Program initialized...")

def loop():
    time.sleep(1)

def end():
    print("[\033[1;32mOK\033[0m] Program terminating...")
    param_hu.state_hu["self"]["status"] = "Offline"
    parser_json.upload_file(param_hu.path_state_hu, param_hu.state_hu)
    connection.stop_daemon()
    #perf_server.stop_daemon()
    sock_server.stop_daemon()
    http_server.stop_daemon()
