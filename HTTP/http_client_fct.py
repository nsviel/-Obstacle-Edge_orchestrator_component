#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from HTTP import http_client
from src import connection
from src import parser_json

import http.client as client
import json


def send_conn_request_ve(command):
    port = param_hu.state_hu["velodium"]["http_server_port"]
    connected = False
    sock = client.HTTPConnection("localhost", port, timeout=0.1)
    try:
        sock.request("GET", command)
        connected = True
    except:
        connected = False
    sock.close()
    return connected

def send_conn_request_ai(command):
    port = param_hu.state_hu["ai"]["http_server_port"]
    connected = False
    sock = client.HTTPConnection("localhost", port, timeout=0.1)
    try:
        sock.request("GET", command)
        connected = True
    except:
        connected = False
    sock.close()
    return connected

def send_conn_request_py(command):
    ip = param_hu.state_hu["pywardium"]["ip"]
    port = param_hu.state_hu["pywardium"]["http_server_port"]
    connected = False
    sock = client.HTTPConnection(ip, port, timeout=0.1)
    try:
        sock.request("GET", command)
        connected = True
    except:
        connected = False
    sock.close()
    return connected

def send_conn_request_ed(command):
    ip = param_hu.state_hu["edge"]["ip"]
    port = param_hu.state_hu["self"]["http_server_port"]
    connected = False
    sock = client.HTTPConnection(ip, port, timeout=0.1)
    try:
        sock.request("GET", command)
        connected = True
    except:
        connected = False
    sock.close()
    return connected

def send_get_state(name):
    connected = param_hu.state_hu["pywardium"]["http_connected"]
    ip = param_hu.state_hu["pywardium"]["ip"]
    port = param_hu.state_hu["pywardium"]["http_server_port"]
    if(connected):
        try:
            sock = client.HTTPConnection(ip, port, timeout=1)
            sock.request("GET", name)
            response = sock.getresponse()
            state = response.read()
            sock.close()
            return state
        except:
            pass

def send_get_command_py(command, sucess):
    connected = param_hu.state_hu["pywardium"]["http_connected"]
    ip = param_hu.state_hu["pywardium"]["ip"]
    port = param_hu.state_hu["pywardium"]["http_server_port"]
    if(connected):
        try:
            sock = client.HTTPConnection(ip, port, timeout=1)
            sock.request("GET", command)
            print(sucess)
        except:
            http_client.connection_closed()

def send_get_command_ve(command):
    connected = param_hu.state_hu["velodium"]["http_connected"]
    port = param_hu.state_hu["velodium"]["http_server_port"]
    if(connected):
        try:
            sock = client.HTTPConnection("localhost", port, timeout=1)
            sock.request("GET", command)
        except:
            http_client.connection_closed()

def send_get_image(path):
    connected = param_hu.state_hu["pywardium"]["http_connected"]
    ip = param_hu.state_hu["pywardium"]["ip"]
    port = param_hu.state_hu["pywardium"]["http_server_port"]
    if(connected):
        try:
            sock = client.HTTPConnection(ip, port, timeout=1)
            sock.request("GET", "/image")
            response = sock.getresponse()
            data_binary = response.read()

            # Save image
            img = open(path, "wb")
            img.write(data_binary)
            img.close()

            sock.close()
        except:
            http_client.connection_closed()

def send_post_request_py(command, payload):
    connected = param_hu.state_hu["pywardium"]["http_connected"]
    ip = param_hu.state_hu["pywardium"]["ip"]
    port = param_hu.state_hu["pywardium"]["http_server_port"]
    header = {"Content-type": "application/json"}
    if(connected):
        try:
            sock = client.HTTPConnection(ip, port, timeout=1)
            sock.request("POST", command, payload, header)
            sock.close()
        except:
            print("[\033[1;31merror\033[0m] Command \033[1;36m%s\033[0m to ip \033[1;36m%s\033[0m port \033[1;36m%d\033[0m failed" % (command, ip, port))

def send_post_request_ve(command, payload):
    connected = param_hu.state_hu["velodium"]["http_connected"]
    port = param_hu.state_hu["velodium"]["http_server_port"]
    header = {"Content-type": "application/json"}
    if(connected):
        try:
            sock = client.HTTPConnection("", port, timeout=1)
            sock.request("POST", command, payload, header)
            sock.close()
        except:
            print("[\033[1;31merror\033[0m] Command \033[1;36m%s\033[0m to ip \033[1;36m%s\033[0m port \033[1;36m%d\033[0m failed" % (command, ip, port))

def send_post_request_ai(command, payload):
    connected = param_hu.state_hu["ai"]["http_connected"]
    port = param_hu.state_hu["ai"]["http_server_port"]
    header = {"Content-type": "application/json"}
    if(connected):
        try:
            sock = client.HTTPConnection("", port, timeout=1)
            sock.request("POST", command, payload, header)
            sock.close()
        except:
            print("[\033[1;31merror\033[0m] Command \033[1;36m%s\033[0m to ip \033[1;36m%s\033[0m port \033[1;36m%d\033[0m failed" % (command, ip, port))
