#---------------------------------------------
from src.param import param_edge
from src.connection.HTTPS import https_client_get

import json
def ask_for_time():
    time_slam = https_client_get.send_command("processing", "/time_slam")
    time_pred = https_client_get.send_command("ai", "/time_pred")

    if(time_slam != None and time_slam != ""):
        time_slam = float(time_slam.decode("utf-8"))
        param_edge.state_network["end_to_end"]["time_slam"] = time_slam

    if(time_pred != None and time_pred != ""):
        time_pred = float(time_pred.decode("utf-8"))
        param_edge.state_network["end_to_end"]["time_ai"] = time_pred

    t1 = param_edge.state_network["end_to_end"]["time_slam"]
    t2 = param_edge.state_network["end_to_end"]["time_ai"]
    duration = t1 + t2
    param_edge.state_network["end_to_end"]["time_total"] = duration
