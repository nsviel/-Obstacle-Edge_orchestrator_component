#---------------------------------------------
from src.param import param_edge
from src.utils import parser_json
from src.utils import terminal

import paho.mqtt.client as mqtt


def on_connection(client, userdata, flags, rc):
    ip = param_edge.state_cloud["operator"]["broker_ip"]
    topic = param_edge.state_cloud["operator"]["mqtt_topic"]
    client.subscribe(topic)
    param_edge.state_cloud["operator"]["broker"]["connected"] = True
    terminal.addDaemon("#", "ON", "MQTT to \033[1;32m%s\033[0m at \033[1;32m%s\033[0m"% (ip, topic))

def on_disconnect(client, userdata, rc):
    topic = param_edge.state_cloud["operator"]["mqtt_topic"]
    client.unsubscribe(topic)
    param_edge.state_cloud["operator"]["broker"]["connected"] = False
    terminal.addDaemon("#", "OFF", "MQTT from \033[1;32m%s\033[0m"% (topic))
