#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from param import param_ext

from src import parser_json


def init_state():
    upload_config_file()
    update_state_file()

def upload_config_file():
    param_hu.sock_port = parser_json.upload_state_lvl2_json(param_hu.path_config, "hubium", "sock_client")
    param_hu.sock_port_listen = parser_json.upload_state_lvl2_json(param_hu.path_config, "hubium", "sock_listen")
    param_hu.sock_port_connection = parser_json.upload_state_lvl2_json(param_hu.path_config, "hubium", "sock_connection")
    param_hu.httpd_port = parser_json.upload_state_lvl2_json(param_hu.path_config, "hubium", "httpd_port")

    param_ext.py_ip = parser_json.upload_state_lvl2_json(param_hu.path_config, "pywardium", "ip")
    param_ext.py_sock_port = parser_json.upload_state_lvl2_json(param_hu.path_config, "pywardium", "port")
    param_ext.edge_port = parser_json.upload_state_lvl2_json(param_hu.path_config, "edge", "port")
    param_ext.mqtt_ip = parser_json.upload_state_lvl2_json(param_hu.path_config, "mqtt", "ip")
    param_ext.mqtt_port = parser_json.upload_state_lvl2_json(param_hu.path_config, "mqtt", "port")
    param_ext.velo_port = parser_json.upload_state_lvl2_json(param_hu.path_config, "velodium", "port")
    param_ext.valeo_ip = parser_json.upload_state_lvl2_json(param_hu.path_config, "valeo", "ip")
    param_ext.valeo_port = parser_json.upload_state_lvl2_json(param_hu.path_config, "valeo", "port")
    param_ext.edge_ip = parser_json.upload_state_lvl2_json(param_hu.path_config, "edge", "ip")

def update_state_file():
    parser_json.update_state_lvl1_json(param_hu.path_state, "status", param_hu.status)
    parser_json.update_state_lvl2_json(param_hu.path_state, "hubium", "sock_client", param_hu.sock_port)
    parser_json.update_state_lvl2_json(param_hu.path_state, "hubium", "sock_listen", param_hu.sock_port_listen)
    parser_json.update_state_lvl2_json(param_hu.path_state, "hubium", "sock_connection", param_hu.sock_port_connection)
    parser_json.update_state_lvl2_json(param_hu.path_state, "hubium", "httpd_port", param_hu.httpd_port)

    parser_json.update_state_lvl2_json(param_hu.path_state, "pywardium", "ip", param_ext.py_ip)
    parser_json.update_state_lvl2_json(param_hu.path_state, "pywardium", "port", param_ext.py_sock_port)
    parser_json.update_state_lvl2_json(param_hu.path_state, "mqtt", "connected", param_ext.mqtt_connected)
    parser_json.update_state_lvl2_json(param_hu.path_state, "mqtt", "ip", param_ext.mqtt_ip)
    parser_json.update_state_lvl2_json(param_hu.path_state, "mqtt", "port", param_ext.mqtt_port)
    parser_json.update_state_lvl2_json(param_hu.path_state, "velodium", "connected", param_ext.velo_connected)
    parser_json.update_state_lvl2_json(param_hu.path_state, "velodium", "port", param_ext.velo_port)
    parser_json.update_state_lvl2_json(param_hu.path_state, "valeo", "ip", param_ext.valeo_ip)
    parser_json.update_state_lvl2_json(param_hu.path_state, "valeo", "port", param_ext.valeo_port)
    parser_json.update_state_lvl2_json(param_hu.path_state, "edge", "ip", param_ext.edge_ip)
    parser_json.update_state_lvl2_json(param_hu.path_state, "edge", "port", param_ext.edge_port)
