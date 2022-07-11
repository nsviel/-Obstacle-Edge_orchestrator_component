#! /usr/bin/python
#---------------------------------------------

from param import classes

from src import parser_json


def publish_test():
    result = classes.connec.mqtt_client.publish(classes.connec.mqtt_topic, classes.connec.mqtt_message)
    if success[0] == 0:
        print(f"Send `{classes.connec.mqtt_message}` to topic `{classes.connec.mqtt_topic}`")
    else:
        print(f"Failed to send message to topic {classes.connec.mqtt_topic}")

def publish_false_alarm():
    if(classes.connec.mqtt_connected):
        msg = parser_json.parse_json(classes.hubium.path_generic + "prediction.json")
        success = classes.connec.mqtt_client.publish(classes.connec.mqtt_topic, msg)
        if success[0] == 0:
            print(f"Send false alarm to topic `{classes.connec.mqtt_topic}`")
        else:
            print(f"Failed to send message to topic {classes.connec.mqtt_topic}")
