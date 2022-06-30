#! /usr/bin/python
#---------------------------------------------

from src import parameter

import paho.mqtt.client as mqtt
import time


def connect():
    client = mqtt.Client()
    client.on_connect = on_connection
    client.on_disconnect = on_disconnect
    client.on_message = subscribe

    client.connect(parameter.mqtt_ip, parameter.mqtt_port)
    client.loop_start()
    parameter.mqtt_client = client

def run():
    publish(parameter.mqtt_client)

def send_false_alarm():
    print("OKKKKKKKKKKKKKKKKKKKKKKK")
    #publish(parameter.mqtt_client)

#Action functions
def on_connection(client, userdata, flags, rc):
    parameter.mqtt_is_connected = True
    client.subscribe("ai_obstacle")

def on_disconnect(client, userdata, rc):
    parameter.mqtt_is_connected = False

def subscribe(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(parameter.mqtt_topic, parameter.mqtt_message)

        # result: [0, 1]
        status = result[0]
        if status == 0:
         print(f"Send `{parameter.mqtt_message}` to topic `{parameter.mqtt_topic}`")
        else:
         print(f"Failed to send message to topic {topic}")
        msg_count += 1
