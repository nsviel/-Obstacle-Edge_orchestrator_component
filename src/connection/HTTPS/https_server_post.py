#---------------------------------------------
# Possible POST command:
# - /sncf_param
# - /edge_param
# - /capture_param
# - /processing_param
# - /ai_param
# - /edge_state
# - /capture_state
#---------------------------------------------

from src.param import param_edge
from src.connection.HTTPS import https_client_post
from src.connection.HTTPS import https_server_fct
from src.connection.HTTPS import https_server_forward
from src.utils import parser_json
from src.utils import command
from src.utils import terminal

import json


def manage_post(self):
    command = str(self.path)
    if(command == '/sncf_param'):
        manage_sncf_param(self)
    elif(command == '/edge_param'):
        manage_edge_param(self)
    elif(command == '/capture_param'):
        manage_capture_param(self)
    elif(command == '/processing_param'):
        manage_processing_param(self)
    elif(command == '/ai_param'):
        manage_ai_param(self)
    elif(command == '/edge_state'):
        manage_edge_state(self)
    elif(command == '/capture_state'):
        manage_capture_state(self)
    else:
        print("[error] HTTP POST command not known")

def manage_sncf_param(self):
    pass

def manage_edge_param(self):
    payload = https_server_fct.retrieprocessing_post_data(self)
    if(payload != None):
        data = json.loads(payload)
        [lvl1, lvl2, lvl3] = https_server_fct.decipher_json(data)
        command.manage_command(lvl1, lvl2, lvl3)
        terminal.addPost("edge", lvl1, lvl2, lvl3)

def manage_capture_param(self):
    payload = https_server_fct.retrieprocessing_post_data(self)
    https_client_post.post_param_payload("capture", payload)

def manage_processing_param(self):
    payload = https_server_fct.retrieprocessing_post_data(self)
    if(payload != None):
        data = json.loads(payload)
        [lvl1, lvl2, lvl3] = https_server_fct.decipher_json(data)
        https_server_forward.forward_processing_post(lvl2, lvl3)
        terminal.addPost("processing", lvl1, lvl2, lvl3)

def manage_ai_param(self):
    payload = https_server_fct.retrieprocessing_post_data(self)
    if(payload != None):
        data = json.loads(payload)
        [lvl1, lvl2, lvl3] = https_server_fct.decipher_json(data)
        https_server_forward.forward_ai_post(lvl2, lvl3)
        terminal.addPost("component_ai", lvl1, lvl2, lvl3)

def manage_edge_state(self):
    payload = https_server_fct.retrieprocessing_post_data(self)
    if(payload != None):
        data = json.loads(payload)
        param_edge.state_edge_1 = data
        parser_json.upload_state()
        terminal.addLog("com", "New state received")

def manage_capture_state(self):
    payload = https_server_fct.retrieprocessing_post_data(self)
    if(payload != None):
        data = json.loads(payload)
        https_client_post.post_state("capture", data)
