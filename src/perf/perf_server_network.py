#---------------------------------------------
from src.param import param_hu
from src.perf import perf_server_iperf

import multiprocessing as mp
import threading
import os
import time


def start_daemon():
    thread_con = threading.Thread(target = thread_perf_server)
    thread_con.start()

def stop_daemon():
    if(param_hu.state_hu["perf"]["iperf_activated"]):
        param_hu.run_thread_perf_server = False
        param_hu.process_server_iperf.terminate()
        param_hu.process_server_iperf.join()
        port = param_hu.state_hu["perf"]["iperf_port"]
        command = 'iperf3 -c 127.0.0.1 -p ' + str(port) + ' -t 1 > /dev/null 2>&1'
        os.system(command)

def thread_perf_server():
    if(param_hu.state_hu["perf"]["iperf_activated"]):
        param_hu.run_thread_perf_server = True
        while param_hu.run_thread_perf_server :
            port = param_hu.state_hu["perf"]["iperf_port"]
            param_hu.process_server_iperf = mp.Process(target = perf_server_iperf.process_perf_server, args = (port,))
            param_hu.process_server_iperf.start()
            param_hu.process_server_iperf.join()
