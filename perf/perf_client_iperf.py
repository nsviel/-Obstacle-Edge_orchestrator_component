#---------------------------------------------
from param import param_hu
from src import parser_json
from src import specific

import iperf3


def process_perf_server(ip, port):
    client = iperf3.Client()
    client.duration = 1
    client.server_hostname = ip
    client.port = port
    client.blksize = 1240
    client.protocol = 'udp'
    client.verbose = False
    client.json_output = True
    result = client.run()
    parse_result(result)
    del client

def print_result(result):
    if(result != None and result.error == None):
        print('')
        print('  started at         {0}'.format(result.time))
        print('  jitter (ms)        {0}'.format(result.jitter_ms))
        print('  Bandwidth  (Mbps)  {0}'.format(result.Mbps))
        print('  Lost packets   {0}'.format(result.lost_packets))
        print('  Lost packets percent   {0}'.format(result.lost_percent))

def parse_result(result):
    if(result != None and result.error == None):
        param_hu.state_perf["cloud_local"]["time"] = result.time
        param_hu.state_perf["cloud_local"]["bandwidth"]["value"] = result.Mbps
        param_hu.state_perf["cloud_local"]["reliability"]["value"] = 100 - result.lost_percent
        param_hu.state_perf["cloud_local"]["jitter"]["value"] = result.jitter_ms
        parser_json.upload_file(param_hu.path_state_perf, param_hu.state_perf)

def compute_net_state(list_bandwidth, list_reliability, list_jitter):
    # Reload network state
    param_hu.state_perf = parser_json.load_data_from_file(param_hu.path_state_perf)
    #------------------

    # Bandwidth
    specific.list_stack(list_bandwidth, param_hu.state_perf["cloud_local"]["bandwidth"]["value"], 10)
    param_hu.state_perf["cloud_local"]["bandwidth"]["min"] = min(list_bandwidth)
    param_hu.state_perf["cloud_local"]["bandwidth"]["max"] = max(list_bandwidth)
    param_hu.state_perf["cloud_local"]["bandwidth"]["mean"] = specific.mean(list_bandwidth)

    # Reliability
    specific.list_stack(list_reliability, param_hu.state_perf["cloud_local"]["reliability"]["value"], 10)
    param_hu.state_perf["cloud_local"]["reliability"]["min"] = min(list_reliability)
    param_hu.state_perf["cloud_local"]["reliability"]["max"] = max(list_reliability)
    param_hu.state_perf["cloud_local"]["reliability"]["mean"] = specific.mean(list_reliability)

    # Jitter
    specific.list_stack(list_jitter, param_hu.state_perf["cloud_local"]["jitter"]["value"], 10)
    param_hu.state_perf["cloud_local"]["jitter"]["min"] = min(list_jitter)
    param_hu.state_perf["cloud_local"]["jitter"]["max"] = max(list_jitter)
    param_hu.state_perf["cloud_local"]["jitter"]["mean"] = specific.mean(list_jitter)
