#! /usr/bin/python
#---------------------------------------------

from param import cla

from src import parser_json

import paho.mqtt.client as mqtt


def test_connection():
    if(cla.connec.sncf_broker_connected == False):
        try:
            cla.connec.mqtt_client.connect(cla.connec.sncf_broker_ip, cla.connec.sncf_broker_port, 5)
            cla.connec.mqtt_client.loop_start()
        except:
            return

def start_client():
    client = mqtt.Client()
    client.on_connect = on_connection
    client.on_disconnect = on_disconnect
    cla.connec.mqtt_client = client

def on_connection(client, userdata, flags, rc):
    cla.connec.sncf_broker_connected = True
    client.subscribe(cla.connec.sncf_mqtt_topic)

def on_disconnect(client, userdata, rc):
    cla.connec.sncf_broker_connected = False
