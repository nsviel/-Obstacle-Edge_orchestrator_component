#! /usr/bin/python
#---------------------------------------------

from param import param_ext
from param import param_hu

from src import parser_json


def publish_test():
    result = param_ext.mqtt_client.publish(param_ext.mqtt_topic, param_ext.mqtt_message)
    if success[0] == 0:
        print(f"Send `{param_ext.mqtt_message}` to topic `{param_ext.mqtt_topic}`")
    else:
        print(f"Failed to send message to topic {param_ext.mqtt_topic}")

def publish_false_alarm():
    if(param_ext.mqtt_connected):
        msg = parser_json.parse_json(param_hu.path_generic + "prediction.json")
        success = param_ext.mqtt_client.publish(param_ext.mqtt_topic, msg)
        if success[0] == 0:
            print(f"Send false alarm to topic `{param_ext.mqtt_topic}`")
        else:
            print(f"Failed to send message to topic {param_ext.mqtt_topic}")
