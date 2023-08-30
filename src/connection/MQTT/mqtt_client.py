#---------------------------------------------
from src.param import param_edge
from src.connection.MQTT import mqtt_class
from src.utils import parser_json
from src.utils import signal

import paho.mqtt.client as mqtt


def test_connection_operator():
    connected = param_edge.state_edge["interface"]["operator"]["broker_connected"]
    if(connected == False):
        try:
            create_client()
            mqtt_connection()
        except:
            mqtt_disconnection()

def create_client():
    client_name = param_edge.state_cloud["operator"]["broker"]["client"]
    client = mqtt.Client(client_name)
    client.on_connect = mqtt_class.on_connection
    client.on_disconnect = mqtt_class.on_disconnect
    param_edge.mqtt_client = client

def mqtt_connection():
    ip = param_edge.state_cloud["operator"]["broker"]["ip"]
    port = param_edge.state_cloud["operator"]["broker"]["port"]
    param_edge.mqtt_client.connect(ip, port)
    param_edge.state_edge["interface"]["operator"]["broker_connected"] = True
    param_edge.mqtt_client.loop_start()

def mqtt_disconnection():
    param_edge.mqtt_client.disconnect()
