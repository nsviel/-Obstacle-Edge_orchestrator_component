#---------------------------------------------
from src.param import param_hu
from src.misc import specific

import datetime
import os


#TODO: refaire cette function

def ping(ip, list_latency):
    # Retrieve latency
    os.system("ping -c 1 -t 1 " + ip + " > src/perf/ping 2>/dev/null")
    with open('src/perf/ping', 'r') as file:
        data = file.read().rstrip()
    id_b = data.find("time=") + 5
    id_e = data.find(" ms")

    # Compute latency
    if(id_b != -1 and id_e != -1):
        latency = float(data[id_b:id_e])
        specific.list_stack(list_latency, latency, 10)
        param_hu.state_perf["cloud_local"]["latency"]["value"] = latency
        param_hu.state_perf["cloud_local"]["latency"]["min"] = min(list_latency)
        param_hu.state_perf["cloud_local"]["latency"]["max"] = max(list_latency)
        param_hu.state_perf["cloud_local"]["latency"]["mean"] = specific.mean(list_latency)
