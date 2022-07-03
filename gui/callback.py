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
