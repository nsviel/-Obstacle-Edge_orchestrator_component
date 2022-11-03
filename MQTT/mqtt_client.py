#---------------------------------------------
from param import param_hu
from MQTT import mqtt_class
from src import parser_json
from src import signal

import paho.mqtt.client as mqtt


def test_sncf_connection():
    connected = param_hu.state_hu["sncf"]["broker_connected"]
    if(connected == False):
        try:
            create_client()
            mqtt_connection()
        except:
            mqtt_disconnection()

def create_client():
    client_name = param_hu.state_hu["sncf"]["mqtt_client"]
    client = mqtt.Client(client_name)
    client.on_connect = mqtt_class.on_connection
    client.on_disconnect = mqtt_class.on_disconnect
    param_hu.mqtt_client = client

def mqtt_connection():
    ip = param_hu.state_hu["sncf"]["broker_ip"]
    port = param_hu.state_hu["sncf"]["broker_port"]
    param_hu.mqtt_client.connect(ip, port)
    # /!\ this line is incompatible with iperf3 server thread
    #param_hu.mqtt_client.loop_start()

def mqtt_disconnection():
    param_hu.mqtt_client.disconnect()
