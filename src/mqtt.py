#! /usr/bin/python
#---------------------------------------------

from param import classes

from src import parser_json

import paho.mqtt.client as mqtt


def test_connection():
    if(classes.connec.mqtt_connected == False):
        try:
            classes.connec.mqtt_client.connect(classes.connec.mqtt_ip, classes.connec.mqtt_port, 5)
            classes.connec.mqtt_client.loop_start()
        except:
            return

def start_init():
    client = mqtt.Client()
    client.on_connect = on_connection
    client.on_disconnect = on_disconnect
    classes.connec.mqtt_client = client

def on_connection(client, userdata, flags, rc):
    classes.connec.mqtt_connected = True
    client.subscribe("ai_obstacle")

def on_disconnect(client, userdata, rc):
    classes.connec.mqtt_connected = False
