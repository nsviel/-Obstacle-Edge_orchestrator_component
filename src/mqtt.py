#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import io

import paho.mqtt.client as mqtt
import time


def test_connection():
    client = mqtt.Client()
    try:
        client.connect(parameter.mqtt_ip, parameter.mqtt_port, 5)
        parameter.mqtt_connected = True
    except:
        parameter.mqtt_connected = False

def connect():
    if(parameter.mqtt_connected):
        client = mqtt.Client()
        client.on_connect = on_connection
        client.on_disconnect = on_disconnect

        client.connect(parameter.mqtt_ip, parameter.mqtt_port)
        client.loop_start()
        parameter.mqtt_client = client

#Action functions
def on_connection(client, userdata, flags, rc):
    parameter.mqtt_connected = True
    client.subscribe("ai_obstacle")

def on_disconnect(client, userdata, rc):
    parameter.mqtt_connected = False

def publish_test(client):
    result = parameter.mqtt_client.publish(parameter.mqtt_topic, parameter.mqtt_message)
    if success[0] == 0:
        print(f"Send `{parameter.mqtt_message}` to topic `{parameter.mqtt_topic}`")
    else:
        print(f"Failed to send message to topic {parameter.mqtt_topic}")

def publish_false_alarm():
    msg = io.parse_json(parameter.path_generic + "prediction.json")
    success = parameter.mqtt_client.publish(parameter.mqtt_topic, msg)
    if success[0] == 0:
        print(f"Send false alarm to topic `{parameter.mqtt_topic}`")
    else:
        print(f"Failed to send message to topic {parameter.mqtt_topic}")
