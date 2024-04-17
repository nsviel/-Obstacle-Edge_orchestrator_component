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

        data = json.dumps(param_edge.state_edge).encode(encoding='utf_8')
        https_server_fct.send_get_response(self, data, "application/json")
    elif(command == '/get_state_ground'):
        data = json.dumps(param_edge.state_ground).encode(encoding='utf_8')
        https_server_fct.send_get_response(self, data, "application/json")
    elif(command == '/get_state_cloud'):
        data = json.dumps(param_edge.state_cloud).encode(encoding='utf_8')
        https_server_fct.send_get_response(self, data, "application/json")
    elif(command == '/get_state_network'):
        data = json.dumps(param_edge.state_network).encode(encoding='utf_8')
        https_server_fct.send_get_response(self, data, "application/json")
    elif(command == '/get_image'):
        get_image(self)
    else:
        print("[error] HTTP GET command not known [%s]"% command)

def get_image(self):
    #path = param_edge.path_image
    path = "engine/build/image.bmp"
    #print(io.is_file_exist(path))
    if(io.is_file_exist(path)):
        try:
            data = io.load_binary(path)
            https_server_fct.send_get_response(self, data, "image/bmp")
        except:
            pass
