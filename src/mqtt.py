#! /usr/bin/python
#---------------------------------------------

from param import param_ext
from param import param_hu

from src import parser_json

import paho.mqtt.client as mqtt


def test_connection():
    if(param_ext.mqtt_connected == False):
        try:
            param_ext.mqtt_client.connect(param_ext.mqtt_ip, param_ext.mqtt_port, 5)
            param_ext.mqtt_client.loop_start()
        except:
            return

def start_init():
    client = mqtt.Client()
    client.on_connect = on_connection
    client.on_disconnect = on_disconnect
    param_ext.mqtt_client = client

def on_connection(client, userdata, flags, rc):
    param_ext.mqtt_connected = True
    parser_json.update_state_lvl2_json(param_hu.path_state, "mqtt", "connected", param_ext.mqtt_connected)
    client.subscribe("ai_obstacle")

def on_disconnect(client, userdata, rc):
    param_ext.mqtt_connected = False
    parser_json.update_state_lvl2_json(param_hu.path_state, "mqtt", "connected", param_ext.mqtt_connected)
