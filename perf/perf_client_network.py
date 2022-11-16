#---------------------------------------------
from param import param_hu
from HTTPS import https_client_get
from perf import perf_client_ping
from perf import perf_client_iperf
from perf import perf_client_module
from src import parser_json
from src import kpi

import multiprocessing as mp
import threading
import time


def start_daemon():
    thread_con = threading.Thread(target = thread_perf_server)
    thread_con.start()

def stop_daemon():
    param_hu.run_thread_perf_client = False
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
        https_client_get.get_state("perf")
        ip = param_hu.state_hu["pywardium"]["ip"]
        port = param_hu.state_hu["pywardium"]["iperf_port"]

        # iperf
        process_iperf(ip, port)
        perf_client_iperf.compute_net_state(list_bandwidth, list_reliability, list_jitter)

        # Ping
        perf_client_ping.ping(ip, list_latency)

        # Time
        perf_client_module.ask_for_time()

        # Make KPI stuff
        kpi.format_state_kpi()
        kpi.send_kpi_to_mongodb()

        # Update state file and sleep one second
        parser_json.upload_file(param_hu.path_state_perf, param_hu.state_perf)
        time.sleep(1)


def process_iperf(ip, port):
    param_hu.process_client_iperf = mp.Process(target = perf_client_iperf.process_perf_server, args = (ip, port))
    param_hu.process_client_iperf.start()
    param_hu.process_client_iperf.join()
