#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import io

import dearpygui.dearpygui as dpg


def callback_event():
    parameter.run = dpg.get_value("bclo")

def callback_parameter():
    parameter.http_port = dpg.get_value("httpp")
    parameter.mqtt_ip = dpg.get_value("mqttip")
    parameter.mqtt_port = dpg.get_value("mqttp")
    parameter.mqtt_topic = dpg.get_value("mqttt")
    parameter.mqtt_message = dpg.get_value("mqttm")

    parameter.port_pywar = dpg.get_value("socketpy")
    parameter.port_velo = dpg.get_value("socketve")
    parameter.port_edge = dpg.get_value("socketed")


def callback_loop():
    nb_frame = io.get_number_file(parameter.path_frame)
    dpg.set_value("cpt_nb_frame", nb_frame)
    nb_pred = io.get_number_file(parameter.path_predic)
    dpg.set_value("cpt_nb_pred", nb_pred)

    file_exist = io.is_file_exist(parameter.path_image)
    if(file_exist):
        dpg.set_value("cpt_image", "OK")
    else:
        dpg.set_value("cpt_image", "-")
    file_exist = io.is_file_exist(parameter.path_geoloc)
    if(file_exist):
        dpg.set_value("cpt_geo", "OK")
    else:
        dpg.set_value("cpt_geo", "-")

    if(parameter.mqtt_is_connected):
        dpg.set_value("smqttsncf", "ON")
    else:
        dpg.set_value("smqttsncf", "OFF")
    if(parameter.http_is_connected):
        dpg.set_value("qhttpserv", "ON")
    else:
        dpg.set_value("qhttpserv", "OFF")
