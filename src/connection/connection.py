#---------------------------------------------
from src.param import param_edge

from src.connection.HTTPS.client import https_client_con
from src.connection.HTTPS.client import https_client_get
from src.connection.MQTT import mqtt_client

from src.utils import parser_json
from src.utils import io
from src.utils import prediction
from src.utils import terminal
from src.state import state
from src.base import daemon

import socket
import threading
import os, os.path


class Connection(daemon.Daemon):
    def __init__(self):
        self.name = "Connection";
        self.run_sleep = 0.5;
        self.mqtt = mqtt_client.MQTT_client()

    def thread_function(self):
        # Test connection
        self.mqtt.test_connection_operator()
        https_client_con.test_connection_slam()
        https_client_con.test_connection_ai()
        https_client_con.test_connection_ground()

        # Update state file
        https_client_get.get_state("ground")
        state.upload_states()
        prediction.format_prediction()
        update_nb_thread()
        update_data()

    def thread_end(self):
        self.mqtt.mqtt_disconnection()

def get_ip_adress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def update_nb_thread():
    param_edge.state_edge["hub"]["info"]["nb_thread"] = threading.active_count()
import os

def update_data():
    path = param_edge.path_frame_dir + "/"
    nb_file = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    param_edge.state_edge["data"]["nb_frame"] = nb_file

def check_port_open(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    is_open = False
    if result == 0:
       is_open = True
    else:
        terminal.addLog("error", "Port \033[1;32m%d\033[0m is closed"% port)
    sock.close()
    return is_open;
