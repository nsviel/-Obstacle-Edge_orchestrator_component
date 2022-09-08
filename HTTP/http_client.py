#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from src import parser_json
from HTTP import http_client_fct


def test_ve_connection():
    connected = http_client_fct.send_conn_request_ve("/test_http_conn")
    if(connected):
        param_hu.state_hu["velodium"]["http_connected"] = True
    else:
        param_hu.state_hu["velodium"]["http_connected"] = False

def test_ai_connection():
    connected = http_client_fct.send_conn_request_ai("/test_http_conn")
    if(connected):
        param_hu.state_hu["ai"]["http_connected"] = True
    else:
        param_hu.state_hu["ai"]["http_connected"] = False

def test_py_connection():
    connected = http_client_fct.send_conn_request_py("/test_http_conn")
    if(connected):
        param_hu.state_hu["pywardium"]["http_connected"] = True
    else:
        param_hu.state_hu["pywardium"]["http_connected"] = False
        param_hu.state_hu["pywardium"]["sock_l1_connected"] = False
        param_hu.state_hu["pywardium"]["sock_l2_connected"] = False
        param_hu.state_py["self"]["status"] = "Offline"
        param_hu.state_py["lidar_1"]["connected"] = False
        param_hu.state_py["lidar_2"]["connected"] = False
        #TODO: faire fonction pour ne modifier que certaines valeurs
        parser_json.upload_file(param_hu.path_state_py, param_hu.state_py)

def test_ed_connection():
    connected = http_client_fct.send_conn_request_ed("/test_http_conn")
    if(connected):
        param_hu.state_hu["edge"]["http_connected"] = True
    else:
        param_hu.state_hu["edge"]["http_connected"] = False
        param_hu.state_hu["edge"]["sock_l1_connected"] = False
        param_hu.state_hu["edge"]["sock_l2_connected"] = False
        param_hu.state_hu["edge"]["status"] = "Offline"
