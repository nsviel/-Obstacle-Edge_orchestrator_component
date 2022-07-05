#! /usr/bin/python
#---------------------------------------------

from param import param_hu
from param import param_ext

from src import parser_json


def init_state():
    upload_config_file()
    update_state_file()

def upload_config_file():
    param_ext.edge_port = parser_json.upload_state_lvl2_json(param_hu.path_config, "edge", "port")
    param_ext.mqtt_ip = parser_json.upload_state_lvl2_json(param_hu.path_config, "mqtt", "ip")
    param_ext.mqtt_port = parser_json.upload_state_lvl2_json(param_hu.path_config, "mqtt", "port")
    param_ext.velo_port = parser_json.upload_state_lvl2_json(param_hu.path_config, "velodium", "port")
    param_ext.valeo_ip = parser_json.upload_state_lvl2_json(param_hu.path_config, "valeo", "ip")
    param_ext.valeo_port = parser_json.upload_state_lvl2_json(param_hu.path_config, "valeo", "port")
    param_ext.edge_ip = parser_json.upload_state_lvl2_json(param_hu.path_config, "edge", "ip")

def update_state_file():
    parser_json.update_state_lvl1_json(param_hu.path_state, "status", "Online")
    parser_json.update_state_lvl2_json(param_hu.path_state, "mqtt", "ip", param_ext.mqtt_ip)
    parser_json.update_state_lvl2_json(param_hu.path_state, "mqtt", "port", param_ext.mqtt_port)
    parser_json.update_state_lvl2_json(param_hu.path_state, "velodium", "port", param_ext.velo_port)
    parser_json.update_state_lvl2_json(param_hu.path_state, "valeo", "ip", param_ext.valeo_ip)
    parser_json.update_state_lvl2_json(param_hu.path_state, "valeo", "port", param_ext.valeo_port)
    parser_json.update_state_lvl2_json(param_hu.path_state, "edge", "ip", param_ext.edge_ip)
    parser_json.update_state_lvl2_json(param_hu.path_state, "edge", "port", param_ext.edge_port)
