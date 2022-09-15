#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from HTTP import http_client_fct
from HTTP import http_client_post


#Test Velodium HTTP connection
def test_ve_con():
    port = param_hu.state_hu["velodium"]["http_server_port"]
    connected = http_client_fct.send_http_ping("localhost", port)
    if(connected):
        param_hu.state_hu["velodium"]["http_connected"] = True
    else:
        param_hu.state_hu["velodium"]["http_connected"] = False

#Test AI HTTP connection
def test_ai_con():
    port = param_hu.state_hu["ai"]["http_server_port"]
    connected = http_client_fct.send_http_ping("localhost", port)
    if(connected):
        param_hu.state_hu["ai"]["http_connected"] = True
    else:
        param_hu.state_hu["ai"]["http_connected"] = False

#Test Pywardium HTTP connection
def test_py_con():
    ip = param_hu.state_hu["pywardium"]["ip"]
    port = param_hu.state_hu["pywardium"]["http_server_port"]
    connected = http_client_fct.send_http_ping(ip, port)
    if(connected):
        connection_py_open()
    else:
        connection_py_close()

def connection_py_open():
    if(param_hu.state_hu["pywardium"]["http_connected"] == False):
        param_hu.state_hu["pywardium"]["http_connected"] = True
        http_client_post.post_param_value("py", "hubium", "ip", param_hu.state_hu["self"]["ip"])

def connection_py_close():
    param_hu.state_hu["pywardium"]["http_connected"] = False
    param_hu.state_hu["pywardium"]["sock_l1_connected"] = False
    param_hu.state_hu["pywardium"]["sock_l2_connected"] = False

#Test Pywardium HTTP connection
def test_ed_con():
    ip = param_hu.state_hu["edge"]["ip"]
    port = param_hu.state_hu["self"]["http_server_port"]
    connected = http_client_fct.send_http_ping(ip, port)
    if(connected):
        connection_ed_open()
    else:
        connection_ed_close()

def connection_ed_open():
    param_hu.state_hu["edge"]["http_connected"] = True

def connection_ed_close():
    param_hu.state_hu["edge"]["http_connected"] = False
    param_hu.state_hu["edge"]["sock_l1_connected"] = False
    param_hu.state_hu["edge"]["sock_l2_connected"] = False
    param_hu.state_hu["edge"]["status"] = "Offline"
