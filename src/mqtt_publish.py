#! /usr/bin/python
#---------------------------------------------

from param import cla

from src import parser_json


def publish_test():
    result = cla.connec.mqtt_client.publish(cla.connec.mqtt_topic, cla.connec.mqtt_message)
    if success[0] == 0:
        print(f"Send `{cla.connec.mqtt_message}` to topic `{cla.connec.mqtt_topic}`")
    else:
        print(f"Failed to send message to topic {cla.connec.mqtt_topic}")

def publish_false_alarm():
    if(cla.connec.mqtt_connected):
        msg = parser_json.parse_json(cla.hubium.path_generic + "prediction.json")
        success = cla.connec.mqtt_client.publish(cla.connec.mqtt_topic, msg)
        if success[0] == 0:
            print(f"Send false alarm to topic `{cla.connec.mqtt_topic}`")
        else:
            print(f"Failed to send message to topic {cla.connec.mqtt_topic}")
