#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from src import parser_json
from HTTP import http_client_fct
from HTTP import http_client_post

import http.client

#-----------------------
#Test Velodium HTTP connection
def test_ve_con():
    port = param_hu.state_hu["velodium"]["http_server_port"]
    client = http.client.HTTPConnection("localhost", port, timeout=0.1)
    try:
        client.request("GET", "/test_http_conn")
        connection_ve_open()
    except:
        connection_ve_close()
    client.close()
def connection_ve_open():
    connected = param_hu.state_hu["velodium"]["http_connected"]
    if(connected == False):
        param_hu.state_hu["velodium"]["http_connected"] = True
def connection_ve_close():
    param_hu.state_hu["velodium"]["http_connected"] = False

#-----------------------
#Test AI HTTP connection
def test_ai_con():
    port = param_hu.state_hu["ai"]["http_server_port"]
    client = http.client.HTTPConnection("localhost", port, timeout=0.1)
    try:
        client.request("GET", "/test_http_conn")
        connection_ai_open()
    except:
        connection_ai_close()
    client.close()
def connection_ai_open():
    connected = param_hu.state_hu["ai"]["http_connected"]
    if(connected == False):
        param_hu.state_hu["ai"]["http_connected"] = True
def connection_ai_close():
    param_hu.state_hu["ai"]["http_connected"] = False

#-----------------------
#Test Pywardium HTTP connection
def test_py_con():
    ip = param_hu.state_hu["pywardium"]["ip"]
    port = param_hu.state_hu["pywardium"]["http_server_port"]
    client = http.client.HTTPConnection(ip, port, timeout=0.1)
    try:
        client.request("GET", "/test_http_conn")
        connection_py_open()
    except:
        connection_py_close()
    client.close()
def connection_py_open():
    connected = param_hu.state_hu["pywardium"]["http_connected"]
    if(connected == False):
        param_hu.state_hu["pywardium"]["http_connected"] = True
        http_client_post.post_param_py("hubium", "ip", param_hu.state_hu["self"]["ip"])
def connection_py_close():
    param_hu.state_hu["pywardium"]["http_connected"] = False
    param_hu.state_hu["pywardium"]["sock_l1_connected"] = False
    param_hu.state_hu["pywardium"]["sock_l2_connected"] = False
    param_hu.state_py["self"]["status"] = "Offline"
    param_hu.state_py["lidar_1"]["connected"] = False
    param_hu.state_py["lidar_2"]["connected"] = False
    #TODO: faire fonction pour ne modifier que certaines valeurs
    parser_json.upload_file(param_hu.path_state_py, param_hu.state_py)

#-----------------------
#Test Pywardium HTTP connection
def test_ed_con():
    ip = param_hu.state_hu["edge"]["ip"]
    port = param_hu.state_hu["self"]["http_server_port"]
    client = http.client.HTTPConnection(ip, port, timeout=0.1)
    try:
        client.request("GET", "/test_http_conn")
        connection_ed_open()
    except:
        connection_ed_close()
    client.close()
def connection_ed_open():
    connected = param_hu.state_hu["edge"]["http_connected"]
    if(connected == False):
        param_hu.state_hu["edge"]["http_connected"] = True
def connection_ed_close():
    param_hu.state_hu["edge"]["http_connected"] = False
    param_hu.state_hu["edge"]["sock_l1_connected"] = False
    param_hu.state_hu["edge"]["sock_l2_connected"] = False
    param_hu.state_hu["edge"]["status"] = "Offline"
