#---------------------------------------------
from param import param_hu
from MQTT import mqtt_publish
from MQTT import mqtt_client


def manage_command(lvl1, lvl2, lvl3):
    if(lvl1 != None and lvl1 != "null"):
        param_hu.state_hu[lvl1][lvl2] = lvl3
        if(lvl1 == "sncf"):
            if(lvl2 == "broker_ip"):
                mqtt_client.mqtt_disconnection()
    else:
        if(lvl2 == "sncf"):
            if(lvl3 == "reset"):
                mqtt_client.mqtt_disconnection()
            if(lvl3 == "false_alarm"):
                mqtt_publish.publish_false_alarm()
