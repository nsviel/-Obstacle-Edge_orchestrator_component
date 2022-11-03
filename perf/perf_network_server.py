#---------------------------------------------
from param import param_hu
from threading import Thread

import multiprocessing as mp

import iperf3
import json
import os

def start_daemon():
    thread_con = Thread(target = thread_perf_server)
    thread_con.start()

def stop_daemon():
    port = param_hu.state_hu["self"]["iperf_port"]
    command = 'iperf3 -c 127.0.0.1 -p ' + str(port) + ' -t 1 > /dev/null 2>&1'
    os.system(command)
    param_hu.run_thread_net = False

def thread_perf_server():
    param_hu.run_thread_net = True
    while param_hu.run_thread_net :
        port = param_hu.state_hu["self"]["iperf_port"]
        process_net = mp.Process(target = process_perf_server, args = (port,))
        process_net.start()
        process_net.join()

def process_perf_server(port):
    server = iperf3.Server()
    server.bind_address = '127.0.0.1'
    server.port = port
    server.verbose = False
    server.json_output = True
    result = server.run()
    parse_result(result)

def parse_result(result):
    try:
        if(result != None and result.error == None):
            print('  bytes transmitted  {0}'.format(result.bytes))
            print('')
            print('Test completed:')
            print('')
            print('  started at         {0}'.format(result.time))
            print('  jitter (ms)        {0}'.format(result.jitter_ms))
            print('  avg cpu load       {0}%\n'.format(result.local_cpu_total))

            print('Average transmitted data in all sorts of networky formats:')
            print('  bits per second      (bps)   {0}'.format(result.bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.MB_s))
    except:
        pass
