#---------------------------------------------
from src.param import param_edge
from src.connection.HTTPS.client import https_client_get

import json
def ask_for_time():
    time_slam = https_client_get.send_command("slam", "/time_slam")
    time_pred = https_client_get.send_command("ai", "/time_pred")

    try:
        if(time_slam != None and time_slam != ""):
            time_slam = float(time_slam.decode("utf-8"))
            param_edge.state_network["time"]["slam"] = time_slam

        if(time_pred != None and time_pred != ""):
            time_pred = float(time_pred.decode("utf-8"))
            param_edge.state_network["time"]["ai"] = time_pred
    except:
        pass

    t1 = param_edge.state_network["time"]["slam"]
    t2 = param_edge.state_network["time"]["ai"]
    duration = t1 + t2
    param_edge.state_network["time"]["total"] = duration
