#---------------------------------------------
from param import param_hu

import http.client


def network_info(dest):
    if(dest == "py" or dest == "perf"):
        ip = param_hu.state_hu["pywardium"]["ip"]
        port = param_hu.state_hu["pywardium"]["http_server_port"]
        connected = param_hu.state_hu["pywardium"]["http_connected"]
    elif(dest == "ve"):
        ip = param_hu.state_hu["velodium"]["ip"]
        port = param_hu.state_hu["velodium"]["http_server_port"]
        connected = param_hu.state_hu["velodium"]["http_connected"]
    elif(dest == "ai"):
        ip = param_hu.state_hu["ai"]["ip"]
        port = param_hu.state_hu["ai"]["http_server_port"]
        connected = param_hu.state_hu["ai"]["http_connected"]
    elif(dest == "ed"):
        ip = param_hu.state_hu["edge"]["ip"]
        port = param_hu.state_hu["self"]["http_server_port"]
        connected = param_hu.state_hu["edge"]["http_connected"]

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
            header = {"Content-type": "text/plain"}
            payload = str(payload)
            client.request("POST", command, payload, header)
            client.close()
        except:
            print("[\033[1;31merror\033[0m] Command \033[1;36m%s\033[0m to ip \033[1;36m%s\033[0m port \033[1;36m%d\033[0m failed" % (command, ip, port))

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
