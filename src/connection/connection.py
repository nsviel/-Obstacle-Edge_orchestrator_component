#---------------------------------------------
from src.param import param_edge

from src.connection.HTTPS import https_client_con
from src.connection.HTTPS import https_client_get
from src.connection.MQTT import mqtt_client
from src.connection.SOCK import sock_client

from src.utils import parser_json
from src.utils import io
from src.utils import prediction
from src.utils import terminal
from src.base import daemon

import socket
import threading
import os, os.path


class Connection(daemon.Daemon):
    def thread_function(self):
        # Test connection
        mqtt_client.test_sncf_connection()
        https_client_con.test_processing_con()
        https_client_con.test_ai_con()
        https_client_con.test_capture_con()
        https_client_con.test_ed_con()

        # Update state file
        https_client_get.get_state("capture")
        parser_json.upload_state()
        sock_client.reset_connnection()
        prediction.format_prediction()
        update_nb_thread()
        update_data()

    name = "Connection";
    run_sleep = 0.5;

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
    param_edge.state_edge["self"]["nb_thread"] = threading.active_count()
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
