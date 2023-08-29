#---------------------------------------------
from src.param import param_edge

import http.client


def network_info(dest):
    ip = ""
    port = 0
    connected = False
    if(dest == "capture" or dest == "network"):
        ip = param_edge.state_ground["capture"]["info"]["ip"]
        port = param_edge.state_ground["capture"]["http"]["server_port"]
        connected = param_edge.state_ground["capture"]["http"]["connected"]
    elif(dest == "processing"):
        ip = param_edge.state_edge["hub"]["info"]["ip"]
        port = param_edge.state_edge["slam"]["http"]["server_port"]
        connected = param_edge.state_edge["slam"]["http"]["connected"]
    elif(dest == "ai"):
        ip = param_edge.state_edge["hub"]["info"]["ip"]
        port = param_edge.state_edge["ai"]["http"]["server_port"]
        connected = param_edge.state_edge["ai"]["http"]["connected"]

    return [ip, port, connected]

def send_https_ping(ip, port):
    client = http.client.HTTPConnection(ip, port, timeout=0.1)
    connected = False
    try:
        client.request("GET", "/test_http_conn")
        connected = True
    except:
        connected = False
    client.close()
    return connected

def send_https_post(ip, port, connected, command, payload):
    if(connected):
        try:
            client = http.client.HTTPConnection(ip, port, timeout=1)
            header = {"Content-type": "application/json"}
            client.request("POST", command, payload, header)
            client.close()
        except:
            print("[\033[1;31merror\033[0m] Command \033[1;36m%s\033[0m to ip \033[1;36m%s\033[0m port \033[1;36m%d\033[0m failed [%s]" % (command, ip, port, payload))

def send_https_get(ip, port, connected, command):
    data = None
    if(connected):
        try:
            client = http.client.HTTPConnection(ip, port, timeout=1)
            client.request("GET", command)
            response = client.getresponse()
            data = response.read()
            client.close()
        except:
            pass
    return data
