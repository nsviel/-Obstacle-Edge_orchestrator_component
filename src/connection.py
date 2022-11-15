#---------------------------------------------
from param import param_hu

from HTTPS import https_client_con
from HTTPS import https_client_get
from MQTT import mqtt_client
from SOCK import sock_client

from src import parser_json
from src import io

import threading
import time
import socket


def start_daemon():
    thread_con = threading.Thread(target = thread_test_connection)
    thread_con.start()

def stop_daemon():
    param_hu.run_thread_con = False

def thread_test_connection():
    param_hu.run_thread_con = True
    while param_hu.run_thread_con:
        # Test connection
        https_client_con.test_ve_con()
        https_client_con.test_ai_con()
        https_client_con.test_py_con()
        https_client_con.test_ed_con()
        mqtt_client.test_sncf_connection()

        # Update state file
        https_client_get.get_state("py")
        parser_json.upload_state()
        sock_client.reset_connnection()
        update_nb_thread()

        # Wait for 1 second
        time.sleep(1)

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
    param_hu.state_hu["self"]["nb_thread"] = threading.active_count()
