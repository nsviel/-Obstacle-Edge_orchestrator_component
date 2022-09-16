#---------------------------------------------
# Possible GET command:
# - /test_http_conn
# - /hu_state
# - /py_state
# - /image
#---------------------------------------------

from param import param_hu
from HTTP import http_server_fct
from src import parser_json
from src import io


def manage_get(self):
    command = str(self.path)
    if(command == '/test_http_conn'):
        self.send_response(200)
    elif(command == '/hu_state'):
        manage_hu_state(self)
    elif(command == '/py_state'):
        manage_py_state(self)
    elif(command == '/image'):
        manage_image(self)

def manage_hu_state(self):
    data = parser_json.load_data_from_file_utf8(param_hu.path_state_hu)
    http_server_fct.send_get_response(self, data, "application/json")

def manage_py_state(self):
    data = parser_json.load_data_from_file_utf8(param_hu.path_state_py)
    http_server_fct.send_get_response(self, data, "application/json")

def manage_image(self):
    if(io.is_file_exist(param_hu.path_image)):
        data = io.load_binary(param_hu.path_image)
        http_server_fct.send_get_response(self, data, "image/bmp")
