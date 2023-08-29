#---------------------------------------------
# Possible GET command:
# - /test_http_conn
# - /edge_state
# - /capture_state
# - /image
#---------------------------------------------

from src.param import param_edge
from src.connection.HTTPS import https_server_fct
from src.utils import parser_json
from src.utils import io


def manage_get(self):
    command = str(self.path)
    if(command == '/test_http_conn'):
        self.send_response(200)
    elif(command == '/edge_state'):
        manage_edge_state(self)
    elif(command == '/capture_state'):
        manage_capture_state(self)
    elif(command == '/network_state'):
        manage_perf_state(self)
    elif(command == '/image'):
        manage_image(self)
    else:
        print("[error] HTTP GET command not known")

def manage_edge_state(self):
    data = parser_json.load_state_utf8(param_capture.path_state_current + "state_edge.json")
    https_server_fct.send_get_response(self, data, "application/json")

def manage_capture_state(self):
    data = parser_json.load_state_utf8(param_capture.path_state_current + "state_ground.json")
    https_server_fct.send_get_response(self, data, "application/json")

def manage_perf_state(self):
    data = parser_json.load_state_utf8(param_capture.path_state_current + "state_network.json")
    https_server_fct.send_get_response(self, data, "application/json")

def manage_image(self):
    if(io.is_file_exist(param_edge.path_image)):
        try:
            data = io.load_binary(param_edge.path_image)
            https_server_fct.send_get_response(self, data, "image/bmp")
        except:
            pass
