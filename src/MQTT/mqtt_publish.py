#---------------------------------------------
from src.param import param_edge
from src.misc import terminal
from src.misc import parser_json


def publish_test():
    topic = param_edge.state_edge["train_operator"]["mqtt_topic"]
    msg = param_edge.mqtt_message
    result = param_edge.mqtt_client.publish(topic, msg)
    if(success[0] == 0):
        terminal.addLog("#", "Send '%s' to topic '%s'"% (msg, topic))
    else:
        terminal.addLog("error", "Failed to send message to topic '%s'" % topic)

def publish_false_alarm():
    connected = param_edge.state_edge["train_operator"]["broker_connected"]
    path_false_alarm = param_edge.path_generic + "prediction.json"
    topic = param_edge.state_edge["train_operator"]["mqtt_topic"]

    if(connected):
        msg = parser_json.load_data_from_file_b(path_false_alarm)
        success = param_edge.mqtt_client.publish(topic, msg)
        if success[0] == 0:
            terminal.addLog("#", "Send false alarm to topic '%s'" % topic)
        else:
            terminal.addLog("error", "Failed to send false alarm to topic '%s'" % topic)
