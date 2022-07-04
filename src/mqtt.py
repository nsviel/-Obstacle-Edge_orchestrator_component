#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import parser_json

import paho.mqtt.client as mqtt


def test_connection():
    if(parameter.mqtt_connected == False):
        try:
            parameter.mqtt_client.connect(parameter.mqtt_ip, parameter.mqtt_port, 5)
            parameter.mqtt_client.loop_start()
        except:
            return
    parser_json.update_state_json("mqtt", "connected", parameter.mqtt_connected)

def start_init():
    client = mqtt.Client()
    client.on_connect = on_connection
    client.on_disconnect = on_disconnect
    parameter.mqtt_client = client

def on_connection(client, userdata, flags, rc):
    parameter.mqtt_connected = True
    client.subscribe("ai_obstacle")

def on_disconnect(client, userdata, rc):
    parameter.mqtt_connected = False
