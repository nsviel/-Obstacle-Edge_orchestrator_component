#! /usr/bin/python
#---------------------------------------------

from param import cla

from src import io
from src import parser_json


def load_configuration():
    upload_config_file()
    update_state_file()

def update_data_file():
    cla.hubium.nb_frame = io.get_number_file(cla.hubium.path_frame)
    cla.hubium.nb_predi = io.get_number_file(cla.hubium.path_predi)

def upload_config_file():
    # Self
    cla.hubium.sock_server_port = parser_json.upload_state_lvl2_json(cla.hubium.path_config, "self", "sock_server_port")
    cla.hubium.http_server_port = parser_json.upload_state_lvl2_json(cla.hubium.path_config, "self", "http_server_port")

    # Pywardium
    cla.connec.py_ip = parser_json.upload_state_lvl2_json(cla.hubium.path_config, "pywardium", "ip")
    cla.connec.py_http_server_port = parser_json.upload_state_lvl2_json(cla.hubium.path_config, "pywardium", "http_server_port")
    cla.connec.py_sock_server_port = parser_json.upload_state_lvl2_json(cla.hubium.path_config, "pywardium", "sock_server_port")

    # Sncf
    cla.connec.sncf_broker_ip = parser_json.upload_state_lvl2_json(cla.hubium.path_config, "sncf", "broker_ip")
    cla.connec.sncf_broker_port = parser_json.upload_state_lvl2_json(cla.hubium.path_config, "sncf", "broker_port")

    # Velodium
    cla.connec.velo_sock_server_port = parser_json.upload_state_lvl2_json(cla.hubium.path_config, "velodium", "sock_server_port")

    # Valeo
    cla.connec.valeo_ip = parser_json.upload_state_lvl2_json(cla.hubium.path_config, "valeo", "ip")

    # Edge
    cla.connec.edge_ip = parser_json.upload_state_lvl2_json(cla.hubium.path_config, "edge", "ip")

def update_state_file():
    # Self
    parser_json.update_state_lvl2_json(cla.hubium.path_state_hu, "self", "status", cla.hubium.status)
    parser_json.update_state_lvl2_json(cla.hubium.path_state_hu, "self", "sock_server_port", cla.hubium.sock_server_port)
    parser_json.update_state_lvl2_json(cla.hubium.path_state_hu, "self", "http_server_port", cla.hubium.http_server_port)
    parser_json.update_state_lvl2_json(cla.hubium.path_state_hu, "self", "nb_frame", cla.hubium.nb_frame)
    parser_json.update_state_lvl2_json(cla.hubium.path_state_hu, "self", "nb_prediction", cla.hubium.nb_predi)

    # Pywardium
    parser_json.update_state_lvl2_json(cla.hubium.path_state_hu, "pywardium", "connected", cla.connec.py_http_connected)
    parser_json.update_state_lvl2_json(cla.hubium.path_state_hu, "pywardium", "ip", cla.connec.py_ip)
    parser_json.update_state_lvl2_json(cla.hubium.path_state_hu, "pywardium", "http_server_port", cla.connec.py_http_server_port)
    parser_json.update_state_lvl2_json(cla.hubium.path_state_hu, "pywardium", "sock_server_port", cla.connec.py_sock_server_port)

    # Sncf
    parser_json.update_state_lvl2_json(cla.hubium.path_state_hu, "sncf", "connected", cla.connec.sncf_broker_connected)
    parser_json.update_state_lvl2_json(cla.hubium.path_state_hu, "sncf", "broker_ip", cla.connec.sncf_broker_ip)
    parser_json.update_state_lvl2_json(cla.hubium.path_state_hu, "sncf", "broker_port", cla.connec.sncf_broker_port)

    # Velodium
    parser_json.update_state_lvl2_json(cla.hubium.path_state_hu, "velodium", "connected", cla.connec.velo_sock_connected)
    parser_json.update_state_lvl2_json(cla.hubium.path_state_hu, "velodium", "sock_server_port", cla.connec.velo_sock_server_port)

    #Valeo
    parser_json.update_state_lvl2_json(cla.hubium.path_state_hu, "valeo", "connected", cla.connec.valeo_connected)
    parser_json.update_state_lvl2_json(cla.hubium.path_state_hu, "valeo", "ip", cla.connec.valeo_ip)

    # Edge
    parser_json.update_state_lvl2_json(cla.hubium.path_state_hu, "edge", "ip", cla.connec.edge_ip)
    parser_json.update_state_lvl2_json(cla.hubium.path_state_hu, "edge", "connected", cla.connec.edge_connected)
