#---------------------------------------------
from src.param import param_edge
from src.connection.MQTT import mqtt_publish
from src.connection.MQTT import mqtt_client


def command_false_alarm():
    mqtt_publish.publish_false_alarm()

def command_broker_reset():
    mqtt_client.mqtt_disconnection()
