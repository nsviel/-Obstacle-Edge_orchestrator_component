#---------------------------------------------
from src.param import param_edge
from src.utils import specific

import subprocess
import datetime
import time
import os


def compute_ping(self):
    data = make_ping()
    if(data != None):
        compute_latency(data, self.list_latency)
        compute_reliability(data, self.list_reliability)

def make_ping():
    ip = param_edge.state_ground["capture"]["info"]["ip"]
    try:
        response = subprocess.check_output(
            ['ping', '-c', '100', '-i', '0.0001', ip],
            stderr=subprocess.DEVNULL,
            universal_newlines=True
        )
    except subprocess.CalledProcessError:
        response = None
    return response

def compute_latency(data, list_latency):
    if(param_edge.state_edge["interface"]["capture"]["http_connected"] == True):
        try:
            id_b = data.find("time=") + 5
            id_e = data.find(" ms")
            latency = float(data[id_b:id_e])
            specific.list_stack(list_latency, latency, 10)

            param_edge.state_network["edge_to_ground"]["latency"]["value"] = latency
            param_edge.state_network["edge_to_ground"]["latency"]["min"] = min(list_latency)
            param_edge.state_network["edge_to_ground"]["latency"]["max"] = max(list_latency)
            param_edge.state_network["edge_to_ground"]["latency"]["mean"] = specific.mean(list_latency)
        except:
            pass
    else:
        param_edge.state_network["edge_to_ground"]["latency"]["value"] = 0
        param_edge.state_network["edge_to_ground"]["latency"]["min"] = 0
        param_edge.state_network["edge_to_ground"]["latency"]["max"] = 0
        param_edge.state_network["edge_to_ground"]["latency"]["mean"] = 0

def compute_reliability(data, list_reliability):
    if(param_edge.state_edge["interface"]["capture"]["http_connected"] == True):
        packetloss = float([x for x in data.split('\n') if x.find('packet loss') != -1][0].split('%')[0].split(' ')[-1])
        reliability = 100 - packetloss
        specific.list_stack(list_reliability, reliability, 10)

        param_edge.state_network["edge_to_ground"]["reliability"]["value"] = reliability;
        param_edge.state_network["edge_to_ground"]["reliability"]["min"] = min(list_reliability)
        param_edge.state_network["edge_to_ground"]["reliability"]["max"] = max(list_reliability)
        param_edge.state_network["edge_to_ground"]["reliability"]["mean"] = specific.mean(list_reliability)
    else:
        param_edge.state_network["edge_to_ground"]["reliability"]["value"] = 0
        param_edge.state_network["edge_to_ground"]["reliability"]["min"] = 0
        param_edge.state_network["edge_to_ground"]["reliability"]["max"] = 0
        param_edge.state_network["edge_to_ground"]["reliability"]["mean"] = 0
