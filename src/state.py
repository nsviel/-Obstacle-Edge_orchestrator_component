#! /usr/bin/python
#---------------------------------------------

from param import param_hu

from src import parser_json


def load_configuration():
    load_json_file()
    upload_config_file()
    reset_value()

def load_json_file():
    param_hu.state_hu = parser_json.load_file(param_hu.path_state_hu)
    param_hu.state_py = parser_json.load_file(param_hu.path_state_py)

def upload_config_file():
    config = parser_json.load_file(param_hu.path_config)
    param_hu.state_hu["self"]["country"] = config["self"]["country"]
    param_hu.state_hu["self"]["edge_id"] = config["self"]["edge_id"]
    param_hu.state_hu["self"]["sock_server_port"] = config["self"]["sock_server_port"]
    param_hu.state_hu["self"]["http_server_port"] = config["self"]["http_server_port"]

    param_hu.state_hu["pywardium"]["ip"] = config["pywardium"]["ip"]
    param_hu.state_hu["pywardium"]["sock_server_port"] = config["pywardium"]["sock_server_port"]
    param_hu.state_hu["pywardium"]["http_server_port"] = config["pywardium"]["http_server_port"]

    param_hu.state_hu["sncf"]["broker_ip"] = config["sncf"]["broker_ip"]
    param_hu.state_hu["sncf"]["broker_port"] = config["sncf"]["broker_port"]

    param_hu.state_hu["velodium"]["sock_server_port"] = config["velodium"]["sock_server_port"]
    param_hu.state_hu["valeo"]["ip"] = config["valeo"]["ip"]
    param_hu.state_hu["edge"]["ip"] = config["edge"]["ip"]

def reset_value():
    param_hu.state_hu["pywardium"]["http_connected"] = False
    param_hu.state_hu["pywardium"]["sock_connected"] = False
    param_hu.state_hu["velodium"]["connected"] = False
    param_hu.state_hu["ai"]["connected"] = False
    param_hu.state_hu["sncf"]["connected"] = False
    param_hu.state_hu["valeo"]["connected"] = False
    param_hu.state_hu["edge"]["connected"] = False
