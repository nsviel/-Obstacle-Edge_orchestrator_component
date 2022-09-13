#! /usr/bin/python
#---------------------------------------------

from param import param_hu

from src import parser_json


def publish_test():
    topic = param_hu.state_hu["sncf"]["mqtt_topic"]
    msg = param_hu.mqtt_message
    result = cla.connec.mqtt_client.publish(topic, msg)
    if success[0] == 0:
        print("[\033[1;32mOK\033[0m] Send '%s' to topic '%s'" % msg, topic)
    else:
        print("[\033[1;31merror\033[0m] Failed to send message to topic '%s'" % topic)

def publish_false_alarm():
    connected = param_hu.state_hu["sncf"]["broker_connected"]
    path_false_alarm = param_hu.path_generic + "prediction.json"
    topic = param_hu.state_hu["sncf"]["mqtt_topic"]
    if(connected):
        msg = parser_json.load_file_to_sock_data(path_false_alarm)
        success = cla.connec.mqtt_client.publish(topic, msg)
        if success[0] == 0:
            print("[\033[1;32mOK\033[0m] Send false alarm to topic '%s'" % topic)
        else:
            print("[\033[1;31m#\033[0m] Failed to send message to topic 'topic'" % topic)
