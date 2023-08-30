#---------------------------------------------
# Possible GET command:
# - /http_ping
# - /get_state_edge
# - /get_state_ground
# - /get_state_cloud
# - /get_state_network
# - /get_image
#---------------------------------------------

from src.param import param_edge
from src.connection.HTTPS.server import https_server_fct
from src.utils import parser_json
from src.utils import io
import json


def manage_get(self):
    command = str(self.path)
    if(command == '/http_ping'):
        self.send_response(200)
    elif(command == '/get_state_edge'):
        state = parser_json.load_state(param_edge.path_state_current + "state_edge.json")
        https_server_fct.send_get_response(self, state, "application/json")
    elif(command == '/get_state_ground'):
        state = parser_json.load_state(param_edge.path_state_current + "state_ground.json")
        https_server_fct.send_get_response(self, state, "application/json")
    elif(command == '/get_state_cloud'):
        state = parser_json.load_state(param_edge.path_state_current + "state_cloud.json")
        https_server_fct.send_get_response(self, state, "application/json")
    elif(command == '/get_state_network'):
        state = parser_json.load_state(param_edge.path_state_current + "state_network.json")
        https_server_fct.send_get_response(self, state, "application/json")
    elif(command == '/get_image'):
        get_image(self)
    else:
        print("[error] HTTP GET command not known [%s]"% command)

def get_image(self):
    if(io.is_file_exist(param_edge.path_image)):
        try:
            data = io.load_binary(param_edge.path_image)
            https_server_fct.send_get_response(self, data, "image/bmp")
        except:
            pass
