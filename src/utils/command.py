#---------------------------------------------
from src.param import param_edge
from src.connection.MQTT import mqtt_publish
from src.connection.MQTT import mqtt_client


def manage_command(lvl1, lvl2, lvl3):
    # 3 level command
    if(lvl1 == "mongo"):
        param_edge.state_network[lvl1][lvl2] = lvl3
    elif(lvl1 != None and lvl1 != "null"):
        param_edge.state_edge_1[lvl1][lvl2] = lvl3
        if(lvl1 == "train_operator"):
            mqtt_client.mqtt_disconnection()
    # Direct command
    else:
        if(lvl2 == "train_operator"):
            if(lvl3 == "reset"):
                mqtt_client.mqtt_disconnection()
            if(lvl3 == "false_alarm"):
                mqtt_publish.publish_false_alarm()
