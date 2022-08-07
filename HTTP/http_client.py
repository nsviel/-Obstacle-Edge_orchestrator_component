#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from HTTP import http_client_fct


def test_py_connection():
    connected = http_client_fct.send_conn_request_py("/test_http_conn")
    if(connected):
        param_hu.state_hu["pywardium"]["http_connected"] = True
    else:
        param_hu.state_hu["pywardium"]["http_connected"] = False
        param_hu.state_hu["pywardium"]["sock_l1_connected"] = False
        param_hu.state_hu["pywardium"]["sock_l2_connected"] = False
        param_hu.state_py["lidar_1"]["connected"] = False
        param_hu.state_py["lidar_2"]["connected"] = False

def test_ve_connection():
    connected = http_client_fct.send_conn_request_ve("/test_http_conn")
    if(connected):
        param_hu.state_hu["velodium"]["http_connected"] = True
    else:
        param_hu.state_hu["velodium"]["http_connected"] = False
