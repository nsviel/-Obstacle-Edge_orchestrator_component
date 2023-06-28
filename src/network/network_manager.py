#---------------------------------------------
from src.param import param_edge
from src.connection.HTTPS import https_client_get
from src.network import network_ping
from src.network import network_module
from src.network import network_mongo
from src.utils import parser_json

import multiprocessing as mp
import threading
import time


def start_daemon():
    thread_con = threading.Thread(target = thread_perf)
    thread_con.start()

def stop_daemon():
    param_edge.thread_perf = False

def thread_perf():
    list_reliability = []
    list_latency = []

    param_edge.thread_perf = True
    while param_edge.thread_perf :
        # Update from py perf state
        update_perf_from_py()

        # Ping
        network_ping.compute_ping(list_latency, list_reliability)

        # System time retrieving
        network_module.ask_for_time()

        # Make mongo stuff
        network_mongo.format_state_kpi()
        network_mongo.send_kpi_to_mongodb()

        # Update state file and sleep one second
        parser_json.upload_file(param_edge.path_state_network, param_edge.state_network)
        time.sleep(param_edge.tic_network)

def update_perf_from_py():
    capture_state_network = https_client_get.get_state_data("network")
    if(capture_state_network == None):
        return

    param_edge.state_network["local_cloud"]["timestamp"] = capture_state_network["local_cloud"]["timestamp"]

    param_edge.state_network["local_cloud"]["throughput"]["value"] = capture_state_network["local_cloud"]["throughput"]["value"]
    param_edge.state_network["local_cloud"]["throughput"]["min"] = capture_state_network["local_cloud"]["throughput"]["min"]
    param_edge.state_network["local_cloud"]["throughput"]["max"] = capture_state_network["local_cloud"]["throughput"]["max"]
    param_edge.state_network["local_cloud"]["throughput"]["mean"] = capture_state_network["local_cloud"]["throughput"]["mean"]

    param_edge.state_network["local_cloud"]["reliability"]["value"] = capture_state_network["local_cloud"]["reliability"]["value"]
    param_edge.state_network["local_cloud"]["reliability"]["min"] = capture_state_network["local_cloud"]["reliability"]["min"]
    param_edge.state_network["local_cloud"]["reliability"]["max"] = capture_state_network["local_cloud"]["reliability"]["max"]
    param_edge.state_network["local_cloud"]["reliability"]["mean"] = capture_state_network["local_cloud"]["reliability"]["mean"]

    param_edge.state_network["local_cloud"]["interruption"]["value"] = capture_state_network["local_cloud"]["interruption"]["value"]
    param_edge.state_network["local_cloud"]["interruption"]["min"] = capture_state_network["local_cloud"]["interruption"]["min"]
    param_edge.state_network["local_cloud"]["interruption"]["max"] = capture_state_network["local_cloud"]["interruption"]["max"]
    param_edge.state_network["local_cloud"]["interruption"]["mean"] = capture_state_network["local_cloud"]["interruption"]["mean"]

    param_edge.state_network["local_cloud"]["latency"]["value"] = capture_state_network["local_cloud"]["latency"]["value"]
    param_edge.state_network["local_cloud"]["latency"]["min"] = capture_state_network["local_cloud"]["latency"]["min"]
    param_edge.state_network["local_cloud"]["latency"]["max"] = capture_state_network["local_cloud"]["latency"]["max"]
    param_edge.state_network["local_cloud"]["latency"]["mean"] = capture_state_network["local_cloud"]["latency"]["mean"]
