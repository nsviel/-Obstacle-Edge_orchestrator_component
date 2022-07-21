#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from src import connection
from src import parser_json


def load_configuration():
    load_json_file()
    init_state()
    load_config_file()
    upload_state()

def load_json_file():
    param_hu.state_hu = parser_json.load_file(param_hu.path_state_hu)
    param_hu.state_py = parser_json.load_file(param_hu.path_state_py)

def init_state():
    param_hu.state_hu["self"]["status"] = "Offline"
    param_hu.state_hu["self"]["ip"] = connection.get_ip_adress()
    param_hu.state_hu["self"]["nb_frame"] = 0
    param_hu.state_hu["self"]["nb_prediction"] = 0
    param_hu.state_hu["self"]["nb_thread"] = 0
    param_hu.state_hu["sncf"]["broker_connected"] = False
    param_hu.state_hu["ai"]["http_connected"] = False
    param_hu.state_hu["velodium"]["sock_connected"] = False
    param_hu.state_hu["pywardium"]["http_connected"] = False
    param_hu.state_hu["pywardium"]["sock_connected"] = False
    param_hu.state_hu["velodium"]["connected"] = False
    param_hu.state_hu["valeo"]["connected"] = False
    param_hu.state_hu["edge"]["connected"] = False

def load_config_file():
    config = parser_json.load_file(param_hu.path_config)
    param_hu.state_hu["self"]["country"] = config["self"]["country"]
    param_hu.state_hu["self"]["edge_id"] = config["self"]["edge_id"]
    param_hu.state_hu["self"]["sock_server_port"] = config["self"]["sock_server_port"]
    param_hu.state_hu["self"]["http_server_port"] = config["self"]["http_server_port"]

    param_hu.state_hu["pywardium"]["ip"] = config["pywardium"]["ip"]
    param_hu.state_hu["pywardium"]["sock_server_port"] = config["pywardium"]["sock_server_port"]
    param_hu.state_hu["pywardium"]["http_server_port"] = config["pywardium"]["http_server_port"]

    param_hu.state_hu["controlium"]["ip"] = config["controlium"]["ip"]
    param_hu.state_hu["controlium"]["sock_server_port"] = config["controlium"]["sock_server_port"]

    param_hu.state_hu["sncf"]["broker_ip"] = config["sncf"]["broker_ip"]
    param_hu.state_hu["sncf"]["broker_port"] = config["sncf"]["broker_port"]

    param_hu.state_hu["velodium"]["sock_server_port"] = config["velodium"]["sock_server_port"]
    param_hu.state_hu["valeo"]["ip"] = config["valeo"]["ip"]
    param_hu.state_hu["edge"]["ip"] = config["edge"]["ip"]

def upload_state():
    parser_json.upload_file(param_hu.path_state_hu, param_hu.state_hu)
