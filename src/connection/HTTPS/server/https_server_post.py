#---------------------------------------------
# Possible POST state:
# - /post_state_edge
# - /post_state_ground
# - /post_state_cloud
# - /post_state_network
# - /post_state_control

# Possible POST command:
# - /post_command_operator
#       - false_alarm
#       - reset
#---------------------------------------------

from src.param import param_edge
from src.connection.HTTPS.client import https_client_post
from src.connection.HTTPS.server import https_server_fct
from src.connection.HTTPS.server import https_server_forward
from src.connection.HTTPS.server import http_command
from src.utils import parser_json
from src.utils import terminal
import json


def manage_post(self):
    command = str(self.path)
    payload = https_server_fct.retrieve_post_data(self)
    if(payload == None):
        return

    # POST state
    if(command == '/post_state_ground'):
        param_edge.state_ground = json.loads(payload)
        https_client_post.post_state("ground", param_edge.state_ground)
    elif(command == '/post_state_edge'):
        param_edge.state_edge = json.loads(payload)
    elif(command == '/post_state_cloud'):
        param_edge.state_cloud = json.loads(payload)
    elif(command == '/post_state_control'):
        param_edge.state_control = json.loads(payload)
    elif(command == '/post_state_network'):
        param_edge.state_network = json.loads(payload)

    # POST command
    elif(command == '/post_command_operator'):
        if(payload == "false_alarm"):
            http_command.command_false_alarm()
        elif(payload == "reset"):
            http_command.command_broker_reset()
    else:
        print("[error] HTTP POST not known [%s]"% command)
