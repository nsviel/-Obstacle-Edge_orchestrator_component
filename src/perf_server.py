#! /usr/bin/python
#---------------------------------------------

from param import param_hu

from threading import Thread

import psutil


def start_daemon():
    thread_con = Thread(target = thread_perf_server)
    thread_con.start()

def stop_daemon():
    param_hu.run_thread_perf = False

def thread_perf_server():
    param_hu.run_thread_perf = True
    while param_hu.run_thread_perf:
        # Compute bandwidth
        inf = "wlp2s0"
        net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
        net_in_1 = net_stat.bytes_recv
        net_out_1 = net_stat.bytes_sent
        time.sleep(1)
        net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
        net_in_2 = net_stat.bytes_recv
        net_out_2 = net_stat.bytes_sent

        net_in = round((net_in_2 - net_in_1) / 1024 / 1024, 3)
        net_out = round((net_out_2 - net_out_1) / 1024 / 1024, 3)
