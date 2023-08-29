#---------------------------------------------
# Possible POST state:
# - /post_state_edge
# - /post_state_ground
# - /post_state_cloud
# - /post_state_network
# - /post_state_control

# Possible POST command:
# - /post_command_xxx
#---------------------------------------------

from src.param import param_edge
from src.connection.HTTPS.client import https_client_post
from src.connection.HTTPS.server import https_server_fct
from src.connection.HTTPS.server import https_server_forward
from src.utils import parser_json
from src.utils import command
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
    elif(command == '/edge_param'):
        data = json.loads(payload)
        [lvl1, lvl2, lvl3] = https_server_fct.decipher_json(data)
        command.manage_command(lvl1, lvl2, lvl3)
        terminal.addPost("edge", lvl1, lvl2, lvl3)
    elif(command == '/capture_param'):
        https_client_post.post_param_payload("capture", payload)
    elif(command == '/processing_param'):
        data = json.loads(payload)
        [lvl1, lvl2, lvl3] = https_server_fct.decipher_json(data)
        https_server_forward.forward_processing_post(lvl2, lvl3)
        terminal.addPost("slam", lvl1, lvl2, lvl3)
    elif(command == '/ai_param'):
        data = json.loads(payload)
        [lvl1, lvl2, lvl3] = https_server_fct.decipher_json(data)
        https_server_forward.forward_ai_post(lvl2, lvl3)
        terminal.addPost("ai", lvl1, lvl2, lvl3)
    else:
        print("[error] HTTP POST not known [%s]"% command)
