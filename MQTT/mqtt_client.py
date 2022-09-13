#! /usr/bin/python
#---------------------------------------------

from param import param_hu

from src import parser_json

import paho.mqtt.client as mqtt


def test_sncf_connection():
    connected = param_hu.state_hu["sncf"]["broker_connected"]
    ip = param_hu.state_hu["sncf"]["broker_ip"]
    port = param_hu.state_hu["sncf"]["broker_port"]

    if(connected == False):
        try:
            param_hu.mqtt_client.connect(ip, port, 1)
            param_hu.mqtt_client.loop_start()
            param_hu.state_hu["sncf"]["status"] = "Online"
            param_hu.state_hu["sncf"]["broker_connected"] = True
        except:
            param_hu.mqtt_client.disconnect()
            param_hu.state_hu["sncf"]["status"] = "Offline"
            param_hu.state_hu["sncf"]["broker_connected"] = False

    print("-------")
    print(ip)
    print(port)
    print(param_hu.state_hu["sncf"]["broker_connected"])

def create_client():
    client = mqtt.Client(param_hu.state_hu["sncf"]["mqtt_client"])
    client.on_connect = on_connection
    client.on_disconnect = on_disconnect
    param_hu.mqtt_client = client
    test_sncf_connection()

def on_connection(client, userdata, flags, rc):
    print("[\033[1;32mOK\033[0m] MQTT connected")
    client.subscribe(param_hu.state_hu["sncf"]["mqtt_topic"])
    param_hu.state_hu["sncf"]["status"] = "Online"
    param_hu.state_hu["sncf"]["broker_connected"] = True

def on_disconnect(client, userdata, rc):
    print("[\033[1;31merror\033[0m] MQTT disconnected")
    param_hu.state_hu["sncf"]["status"] = "Offline"
    param_hu.state_hu["sncf"]["broker_connected"] = False
