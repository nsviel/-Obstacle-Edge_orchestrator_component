#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import io


def publish_test():
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
