#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import callback

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


def build_parameter():
    build_connection()

def build_connection():
    dpg.add_text("Connection", color=(125, 125, 125))
    dpg.add_input_text(tag="httpp", label="HTTP port", default_value=parameter.http_port, width=125, callback=callback.callback_parameter);

    dpg.add_text("")
    dpg.add_input_text(tag="mqttip", label="MQTT IP", default_value=parameter.mqtt_ip, width=125, callback=callback.callback_parameter);
    dpg.add_input_text(tag="mqttp", label="MQTT port", default_value=parameter.mqtt_port, width=125, callback=callback.callback_parameter);
    dpg.add_input_text(tag="mqttt", label="MQTT topic", default_value=parameter.mqtt_topic, width=125, callback=callback.callback_parameter);
    dpg.add_input_text(tag="mqttm", label="MQTT message", default_value=parameter.mqtt_message, width=125, callback=callback.callback_parameter);
