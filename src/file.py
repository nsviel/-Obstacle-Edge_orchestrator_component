#! /usr/bin/python
#---------------------------------------------

from param import classes

from src import parser_json


def init_state():
    upload_config_file()
    update_state_file()

def upload_config_file():
    classes.hubium.sock_port = parser_json.upload_state_lvl2_json(classes.hubium.path_config, "hubium", "sock_client")
    classes.hubium.sock_port_listen = parser_json.upload_state_lvl2_json(classes.hubium.path_config, "hubium", "sock_listen")
    classes.hubium.sock_port_connection = parser_json.upload_state_lvl2_json(classes.hubium.path_config, "hubium", "sock_connection")
    classes.hubium.http_server_port = parser_json.upload_state_lvl2_json(classes.hubium.path_config, "hubium", "http_server_port")

    classes.connec.py_ip = parser_json.upload_state_lvl2_json(classes.hubium.path_config, "pywardium", "ip")
    classes.connec.py_sock_port = parser_json.upload_state_lvl2_json(classes.hubium.path_config, "pywardium", "port")
    classes.connec.edge_port = parser_json.upload_state_lvl2_json(classes.hubium.path_config, "edge", "port")
    classes.connec.mqtt_ip = parser_json.upload_state_lvl2_json(classes.hubium.path_config, "mqtt", "ip")
    classes.connec.mqtt_port = parser_json.upload_state_lvl2_json(classes.hubium.path_config, "mqtt", "port")
    classes.connec.velo_port = parser_json.upload_state_lvl2_json(classes.hubium.path_config, "velodium", "port")
    classes.connec.valeo_ip = parser_json.upload_state_lvl2_json(classes.hubium.path_config, "valeo", "ip")
    classes.connec.edge_ip = parser_json.upload_state_lvl2_json(classes.hubium.path_config, "edge", "ip")

def update_state_file():
    parser_json.update_state_lvl1_json(classes.hubium.path_state, "status", classes.hubium.status)
    parser_json.update_state_lvl2_json(classes.hubium.path_state, "hubium", "sock_client", classes.hubium.sock_port)
    parser_json.update_state_lvl2_json(classes.hubium.path_state, "hubium", "sock_listen", classes.hubium.sock_port_listen)
    parser_json.update_state_lvl2_json(classes.hubium.path_state, "hubium", "sock_connection", classes.hubium.sock_port_connection)
    parser_json.update_state_lvl2_json(classes.hubium.path_state, "hubium", "http_server_port", classes.hubium.http_server_port)

    parser_json.update_state_lvl2_json(classes.hubium.path_state, "pywardium", "ip", classes.connec.py_ip)
    parser_json.update_state_lvl2_json(classes.hubium.path_state, "pywardium", "port", classes.connec.py_sock_port)
    parser_json.update_state_lvl2_json(classes.hubium.path_state, "mqtt", "connected", classes.connec.mqtt_connected)
    parser_json.update_state_lvl2_json(classes.hubium.path_state, "mqtt", "ip", classes.connec.mqtt_ip)
    parser_json.update_state_lvl2_json(classes.hubium.path_state, "mqtt", "port", classes.connec.mqtt_port)
    parser_json.update_state_lvl2_json(classes.hubium.path_state, "velodium", "connected", classes.connec.velo_connected)
    parser_json.update_state_lvl2_json(classes.hubium.path_state, "velodium", "port", classes.connec.velo_port)
    parser_json.update_state_lvl2_json(classes.hubium.path_state, "valeo", "ip", classes.connec.valeo_ip)
    parser_json.update_state_lvl2_json(classes.hubium.path_state, "edge", "ip", classes.connec.edge_ip)
    parser_json.update_state_lvl2_json(classes.hubium.path_state, "edge", "port", classes.connec.edge_port)
