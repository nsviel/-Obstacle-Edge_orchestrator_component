#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import callback

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


def build_parameter():
    dpg.add_text("Connection", color=(125, 125, 125))
    dpg.add_input_text(tag="httpp", label="HTTP server port", default_value=parameter.http_port, width=125, callback=callback.callback_parameter);

    dpg.add_text("")
    dpg.add_input_text(tag="socketpy", label="Socket Pywardium port", default_value=parameter.port_pywar, width=125, callback=callback.callback_parameter);
    dpg.add_input_text(tag="socketve", label="Socket Velodium port", default_value=parameter.port_velo, width=125, callback=callback.callback_parameter);
    dpg.add_input_text(tag="socketed", label="Socket Edge port", default_value=parameter.port_edge, width=125, callback=callback.callback_parameter);

    dpg.add_text("")
    dpg.add_input_text(tag="mqttip", label="MQTT IP", default_value=parameter.mqtt_ip, width=125, callback=callback.callback_parameter);
    dpg.add_input_text(tag="mqttp", label="MQTT port", default_value=parameter.mqtt_port, width=125, callback=callback.callback_parameter);
    dpg.add_input_text(tag="mqttt", label="MQTT topic", default_value=parameter.mqtt_topic, width=125, callback=callback.callback_parameter);
    dpg.add_input_text(tag="mqttm", label="MQTT message", default_value=parameter.mqtt_message, width=125, callback=callback.callback_parameter);
