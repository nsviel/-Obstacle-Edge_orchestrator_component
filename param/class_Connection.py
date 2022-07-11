#! /usr/bin/python
#---------------------------------------------


class Connection:
    #Pywardium
    py_ip = ""
    py_http_server_port = 1
    py_http_connected = False

    # Velodium
    velo_ip = '127.0.0.1'
    velo_sock_server_port = 1
    velo_sock_connected = False

    # AI
    ai_connected = False

    # Sncf
    sncf_broker_connected = False
    sncf_broker_ip = '127.0.0.1'
    sncf_broker_port = 1
    sncf_mqtt_client  = None
    sncf_mqtt_topic = 'ai_obstacle'
    sncf_mqtt_msg = 'hello world'

    # Valeo
    valeo_ip = '127.0.0.1'
    valeo_connected = False

    # Edge
    edge_ip = '127.0.0.1'
    edge_connected = False

    def reset(self):
        self.py_http_connected = False
        self.velo_sock_connected = False
        self.sncf_broker_connected = False
        self.ai_connected = False
