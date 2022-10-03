#---------------------------------------------
# Possible POST command:
# - /sncf_param
# - /hu_param
# - /py_param
# - /ve_param
# - /ai_param
# - /hu_state
# - /py_state
#---------------------------------------------

from param import param_hu
from HTTPS import https_client_post
from HTTPS import https_server_fct
from HTTPS import https_server_forward
from src import parser_json
from src import command

import json


def manage_post(self):
    command = str(self.path)
    if(command == '/sncf_param'):
        manage_sncf_param(self)
    elif(command == '/hu_param'):
        manage_hu_param(self)
    elif(command == '/py_param'):
        manage_py_param(self)
    elif(command == '/ve_param'):
        manage_ve_param(self)
    elif(command == '/ai_param'):
        manage_ai_param(self)
    elif(command == '/hu_state'):
        manage_hu_state(self)
    elif(command == '/py_state'):
        manage_py_state(self)

def manage_sncf_param(self):
    pass

def manage_hu_param(self):
    payload = https_server_fct.retrieve_post_data(self)
    if(payload != None):
        data = json.loads(payload)
        [lvl1, lvl2, lvl3] = https_server_fct.decipher_json(data)
        command.manage_command(lvl1, lvl2, lvl3)

def manage_py_param(self):
    payload = https_server_fct.retrieve_post_data(self)
    https_client_post.post_param_payload("py", payload)

def manage_ve_param(self):
    payload = https_server_fct.retrieve_post_data(self)
    if(payload != None):
        data = json.loads(payload)
        [lvl1, lvl2, lvl3] = https_server_fct.decipher_json(data)
        https_server_forward.forward_ve_post(lvl2, lvl3)

def manage_ai_param(self):
    payload = https_server_fct.retrieve_post_data(self)
    if(payload != None):
        data = json.loads(payload)
        [lvl1, lvl2, lvl3] = https_server_fct.decipher_json(data)
        https_server_forward.forward_ai_post(lvl2, lvl3)

def manage_hu_state(self):
    payload = https_server_fct.retrieve_post_data(self)
    if(payload != None):
        data = json.loads(payload)
        param_hu.state_hu = data
        parser_json.upload_state()
        param_hu.state_hu["sncf"]["broker_connected"] = False

def manage_py_state(self):
    payload = https_server_fct.retrieve_post_data(self)
    if(payload != None):
        data = json.loads(payload)
        https_client_post.post_state("py", data)
