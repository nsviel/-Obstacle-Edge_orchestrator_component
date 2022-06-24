#! /usr/bin/python
#---------------------------------------------

from src import mqtt_config
import paho.mqtt.client as mqtt

import time


#Client function
def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

def connect_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connection
    client.on_message = subscribe

    client.connect(mqtt_config.ip, mqtt_config.port, 60)
    return client

#Action functions
def on_connection(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("ai_obstacle")
def subscribe(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(mqtt_config.topic, mqtt_config.message)

        # result: [0, 1]
        status = result[0]
        if status == 0:
         print(f"Send `{mqtt_config.message}` to topic `{mqtt_config.topic}`")
        else:
         print(f"Failed to send message to topic {topic}")
        msg_count += 1
