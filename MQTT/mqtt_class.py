#---------------------------------------------
from param import param_hu

from src import parser_json

import paho.mqtt.client as mqtt


def on_connection(client, userdata, flags, rc):
    topic = param_hu.state_hu["sncf"]["mqtt_topic"]
    client.subscribe(topic)
    param_hu.state_hu["sncf"]["broker_connected"] = True
    print("[\033[1;32mOK\033[0m] MQTT \033[1;32mconnected\033[0m")

def on_disconnect(client, userdata, rc):
    topic = param_hu.state_hu["sncf"]["mqtt_topic"]
    client.unsubscribe(topic)
    param_hu.state_hu["sncf"]["broker_connected"] = False
    print("[\033[1;32mOK\033[0m] MQTT \033[1;31mdisconnected\033[0m")
