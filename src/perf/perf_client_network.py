#---------------------------------------------
from src.param import param_hu
from src.HTTPS import https_client_get
from src.perf import perf_client_ping
from src.perf import perf_client_iperf
from src.perf import perf_client_module
from src.misc import parser_json
from src.misc import kpi

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
        https_client_get.get_state("perf")
        ip = param_hu.state_py["self"]["ip"]
        port = param_hu.state_py["perf"]["iperf_port"]

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
    if(param_hu.state_hu["perf"]["iperf_activated"]):
        param_hu.process_client_iperf = mp.Process(target = perf_client_iperf.process_perf_client, args = (ip, port))
        param_hu.process_client_iperf.start()
        param_hu.process_client_iperf.join()
