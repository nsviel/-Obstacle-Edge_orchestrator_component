#---------------------------------------------
from src.param import param_hu
from src.HTTPS import https_client_get
from src.perf import perf_client_ping
from src.perf import perf_client_iperf
from src.perf import perf_client_module
from src.misc import parser_json
from src.perf import perf_mongo

import multiprocessing as mp
import threading
import time


def start_daemon():
    thread_con = threading.Thread(target = thread_perf_server)
    thread_con.start()

def stop_daemon():
    param_hu.run_thread_perf_client = False
    if(param_hu.state_hu["perf"]["iperf_activated"]):
        param_hu.process_client_iperf.terminate()
        param_hu.process_client_iperf.join()

def thread_perf_server():
    list_bandwidth = []
    list_reliability = []
    list_jitter = []
    list_latency = []

    param_hu.run_thread_perf_client = True
    while param_hu.run_thread_perf_client :
        # Get the actual perf json from Pywardium
        ip = param_hu.state_py["self"]["ip"]
        port = param_hu.state_py["perf"]["iperf_port"]
        
        # Update from py perf state
        update_perf_from_py()

        # iperf
        process_iperf(ip, port)
        perf_client_iperf.compute_net_state(list_bandwidth, list_reliability, list_jitter)

        # Ping
        perf_client_ping.ping(ip, list_latency)

        # Time
        perf_client_module.ask_for_time()

        # Make KPI stuff
        perf_mongo.format_state_kpi()
        perf_mongo.send_kpi_to_mongodb()

        # Update state file and sleep one second
        parser_json.upload_file(param_hu.path_state_perf, param_hu.state_perf)
        time.sleep(1)

def process_iperf(ip, port):
    if(param_hu.state_hu["perf"]["iperf_activated"]):
        param_hu.process_client_iperf = mp.Process(target = perf_client_iperf.process_perf_client, args = (ip, port))
        param_hu.process_client_iperf.start()
        param_hu.process_client_iperf.join()

def update_perf_from_py():
    py_state_perf = https_client_get.get_state_data("perf")

    param_hu.state_perf["local_cloud"]["time"] = py_state_perf["local_cloud"]["time"]

    param_hu.state_perf["local_cloud"]["bandwidth"]["value"] = py_state_perf["local_cloud"]["bandwidth"]["value"]
    param_hu.state_perf["local_cloud"]["bandwidth"]["min"] = py_state_perf["local_cloud"]["bandwidth"]["min"]
    param_hu.state_perf["local_cloud"]["bandwidth"]["max"] = py_state_perf["local_cloud"]["bandwidth"]["max"]
    param_hu.state_perf["local_cloud"]["bandwidth"]["mean"] = py_state_perf["local_cloud"]["bandwidth"]["mean"]

    param_hu.state_perf["local_cloud"]["reliability"]["value"] = py_state_perf["local_cloud"]["reliability"]["value"]
    param_hu.state_perf["local_cloud"]["reliability"]["min"] = py_state_perf["local_cloud"]["reliability"]["min"]
    param_hu.state_perf["local_cloud"]["reliability"]["max"] = py_state_perf["local_cloud"]["reliability"]["max"]
    param_hu.state_perf["local_cloud"]["reliability"]["mean"] = py_state_perf["local_cloud"]["reliability"]["mean"]

    param_hu.state_perf["local_cloud"]["jitter"]["value"] = py_state_perf["local_cloud"]["jitter"]["value"]
    param_hu.state_perf["local_cloud"]["jitter"]["min"] = py_state_perf["local_cloud"]["jitter"]["min"]
    param_hu.state_perf["local_cloud"]["jitter"]["max"] = py_state_perf["local_cloud"]["jitter"]["max"]
    param_hu.state_perf["local_cloud"]["jitter"]["mean"] = py_state_perf["local_cloud"]["jitter"]["mean"]

    param_hu.state_perf["local_cloud"]["interruption"]["value"] = py_state_perf["local_cloud"]["interruption"]["value"]
    param_hu.state_perf["local_cloud"]["interruption"]["min"] = py_state_perf["local_cloud"]["interruption"]["min"]
    param_hu.state_perf["local_cloud"]["interruption"]["max"] = py_state_perf["local_cloud"]["interruption"]["max"]
    param_hu.state_perf["local_cloud"]["interruption"]["mean"] = py_state_perf["local_cloud"]["interruption"]["mean"]

    param_hu.state_perf["local_cloud"]["latency"]["value"] = py_state_perf["local_cloud"]["latency"]["value"]
    param_hu.state_perf["local_cloud"]["latency"]["min"] = py_state_perf["local_cloud"]["latency"]["min"]
    param_hu.state_perf["local_cloud"]["latency"]["max"] = py_state_perf["local_cloud"]["latency"]["max"]
    param_hu.state_perf["local_cloud"]["latency"]["mean"] = py_state_perf["local_cloud"]["latency"]["mean"]
