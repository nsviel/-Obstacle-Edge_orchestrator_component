#---------------------------------------------
from src.param import param_edge
from src.utils import parser_json
from src.utils import signal
from src.utils import terminal
import paho.mqtt.client as mqtt


class MQTT_client():
    def __init__(self):
        self.is_connected = False
        self.mqtt_client  = None

    def test_connection_operator(self):
        param_edge.state_edge["interface"]["operator"]["broker_connected"] = self.is_connected
        if(self.is_connected == False):
            try:
                self.create_client()
                self.mqtt_connection()
            except:
                self.mqtt_disconnection()

    # Connection function
    def create_client(self):
        client_name = param_edge.state_cloud["operator"]["broker"]["client"]
        self.client = mqtt.Client(client_name)
        self.client.on_connect = self.on_connection
        self.client.on_disconnect = self.on_disconnect
    def mqtt_connection(self):
        ip = param_edge.state_cloud["operator"]["info"]["ip"]
        port = param_edge.state_cloud["operator"]["broker"]["port"]
        self.client.connect(ip, port)
        self.client.loop_start()
    def mqtt_disconnection(self):
        self.client.disconnect()
    def on_connection(self, a, b, c, d):
        ip = param_edge.state_cloud["operator"]["info"]["ip"]
        topic = param_edge.state_cloud["operator"]["broker"]["topic"]
        self.client.subscribe(topic)
        self.is_connected = True
        terminal.addDaemon("#", "ON", "MQTT to \033[1;32m%s\033[0m at \033[1;32m%s\033[0m"% (ip, topic))
    def on_disconnect(self, a, b, c):
        topic = param_edge.state_cloud["operator"]["broker"]["topic"]
        self.client.unsubscribe(topic)
        self.client.disconnect()
        self.is_connected = False
        terminal.addDaemon("#", "OFF", "MQTT from \033[1;32m%s\033[0m"% (topic))

    # Publish function
    def publish_false_alarm(self):
        path_false_alarm = param_edge.path_generic + "prediction.json"
        topic = param_edge.state_cloud["operator"]["broker"]["topic"]
        if(self.is_connected):
            msg = parser_json.load_data_from_file_b(path_false_alarm)
            success = self.client.publish(topic, msg)
            if(success[0] == 0):
                terminal.addLog("#", "False alarm to topic '%s' sent" % topic)
            else:
                terminal.addLog("error", "Failed to send false alarm to topic '%s'" % topic)
