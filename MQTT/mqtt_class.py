#---------------------------------------------
from param import param_hu

from src import parser_json
from src import terminal

import paho.mqtt.client as mqtt


def on_connection(client, userdata, flags, rc):
    ip = param_hu.state_hu["sncf"]["broker_ip"]
    topic = param_hu.state_hu["sncf"]["mqtt_topic"]
    client.subscribe(topic)
    param_hu.state_hu["sncf"]["broker_connected"] = True
    terminal.addDaemon("#", "ON", "MQTT to \033[1;32m%s\033[0m at \033[1;32m%s\033[0m"% (ip, topic))

def on_disconnect(client, userdata, rc):
    topic = param_hu.state_hu["sncf"]["mqtt_topic"]
    client.unsubscribe(topic)
    param_hu.state_hu["sncf"]["broker_connected"] = False
    terminal.addDaemon("#", "OFF", "MQTT from \033[1;32m%s\033[0m"% (topic))
