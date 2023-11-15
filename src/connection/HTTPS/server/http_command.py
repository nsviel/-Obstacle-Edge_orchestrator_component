#---------------------------------------------
from src.param import param_edge
from src import loop


def command_false_alarm():
    loop.loop.daemons.daemon_connection.mqtt.publish_false_alarm()

def command_broker_reset():
    loop.loop.daemons.daemon_connection.mqtt.mqtt_disconnection()
