#! /usr/bin/python
#---------------------------------------------

from param import param_hu

from src import parser_json

import paho.mqtt.client as mqtt


def test_connection():
    connected = param_hu.state_hu["sncf"]["connected"]
    ip = param_hu.state_hu["sncf"]["broker_ip"]
    port = param_hu.state_hu["sncf"]["broker_port"]
    if(connected == False):
        try:
            param_hu.mqtt_client.connect(ip, port, 5)
            param_hu.mqtt_client.loop_start()
        except:
            pass

def start_client():
    client = mqtt.Client()
    client.on_connect = on_connection
    client.on_disconnect = on_disconnect
    param_hu.mqtt_client = client

def on_connection(client, userdata, flags, rc):
    param_hu.state_hu["sncf"]["connected"] = True
    client.subscribe(param_hu.state_hu["sncf"]["mqtt_topic"])

def on_disconnect(client, userdata, rc):
    param_hu.state_hu["sncf"]["connected"] = False
