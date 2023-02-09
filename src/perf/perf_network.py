#---------------------------------------------
from src.param import param_hu
from src.HTTPS import https_client_get
from src.perf import perf_ping
from src.perf import perf_module
from src.perf import perf_mongo
from src.misc import parser_json

import multiprocessing as mp
import threading
import time


def start_daemon():
    thread_con = threading.Thread(target = thread_perf)
    thread_con.start()

def stop_daemon():
    param_hu.thread_perf = False

def thread_perf():
    list_reliability = []
    list_latency = []

    param_hu.thread_perf = True
    while param_hu.thread_perf :
        # Update from py perf state
        update_perf_from_py()

        # Ping
        perf_ping.compute_ping(list_latency, list_reliability)

        # System time retrieving
        perf_module.ask_for_time()

        # Make mongo stuff
        perf_mongo.format_state_kpi()
        perf_mongo.send_kpi_to_mongodb()

        # Update state file and sleep one second
        parser_json.upload_file(param_hu.path_state_perf, param_hu.state_perf)
        time.sleep(param_hu.tic_network)

def update_perf_from_py():
    py_state_perf = https_client_get.get_state_data("perf")
    if(py_state_perf == None):
        return

    param_hu.state_perf["local_cloud"]["timestamp"] = py_state_perf["local_cloud"]["timestamp"]

    param_hu.state_perf["local_cloud"]["throughput"]["value"] = py_state_perf["local_cloud"]["throughput"]["value"]
    param_hu.state_perf["local_cloud"]["throughput"]["min"] = py_state_perf["local_cloud"]["throughput"]["min"]
    param_hu.state_perf["local_cloud"]["throughput"]["max"] = py_state_perf["local_cloud"]["throughput"]["max"]
    param_hu.state_perf["local_cloud"]["throughput"]["mean"] = py_state_perf["local_cloud"]["throughput"]["mean"]

    param_hu.state_perf["local_cloud"]["reliability"]["value"] = py_state_perf["local_cloud"]["reliability"]["value"]
    param_hu.state_perf["local_cloud"]["reliability"]["min"] = py_state_perf["local_cloud"]["reliability"]["min"]
    param_hu.state_perf["local_cloud"]["reliability"]["max"] = py_state_perf["local_cloud"]["reliability"]["max"]
    param_hu.state_perf["local_cloud"]["reliability"]["mean"] = py_state_perf["local_cloud"]["reliability"]["mean"]

    param_hu.state_perf["local_cloud"]["interruption"]["value"] = py_state_perf["local_cloud"]["interruption"]["value"]
    param_hu.state_perf["local_cloud"]["interruption"]["min"] = py_state_perf["local_cloud"]["interruption"]["min"]
    param_hu.state_perf["local_cloud"]["interruption"]["max"] = py_state_perf["local_cloud"]["interruption"]["max"]
    param_hu.state_perf["local_cloud"]["interruption"]["mean"] = py_state_perf["local_cloud"]["interruption"]["mean"]

    param_hu.state_perf["local_cloud"]["latency"]["value"] = py_state_perf["local_cloud"]["latency"]["value"]
    param_hu.state_perf["local_cloud"]["latency"]["min"] = py_state_perf["local_cloud"]["latency"]["min"]
    param_hu.state_perf["local_cloud"]["latency"]["max"] = py_state_perf["local_cloud"]["latency"]["max"]
    param_hu.state_perf["local_cloud"]["latency"]["mean"] = py_state_perf["local_cloud"]["latency"]["mean"]
