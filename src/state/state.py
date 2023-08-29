#---------------------------------------------
from src.param import param_edge
from src.connection import connection
from src.utils import parser_json
from src.utils import terminal
import json

def load_configuration():
    load_json_file()
    terminal.addLog("#", "Configuration loaded")

def load_json_file():
    param_edge.state_ground = parser_json.load_state(param_edge.path_state_initial + "state_ground.json")
    param_edge.state_edge = parser_json.load_state(param_edge.path_state_initial + "state_edge.json")
    param_edge.state_control = parser_json.load_state(param_edge.path_state_initial + "state_control.json")
    param_edge.state_network = parser_json.load_state(param_edge.path_state_initial + "state_network.json")
    param_edge.state_cloud = parser_json.load_state(param_edge.path_state_initial + "state_cloud.json")
    param_edge.state_kpi = parser_json.load_state(param_edge.path_state_initial + "state_kpi.json")
    param_edge.state_prediction = parser_json.load_state(param_edge.path_state_initial + "state_prediction.json")
    
def upload_states():
    parser_json.upload_file(param_edge.path_state_current + "state_ground.json", param_edge.state_ground)
    parser_json.upload_file(param_edge.path_state_current + "state_edge.json", param_edge.state_edge)
    parser_json.upload_file(param_edge.path_state_current + "state_control.json", param_edge.state_control)
    parser_json.upload_file(param_edge.path_state_current + "state_network.json", param_edge.state_network)
    parser_json.upload_file(param_edge.path_state_current + "state_cloud.json", param_edge.state_cloud)
    parser_json.upload_file(param_edge.path_state_current + "state_kpi.json", param_edge.state_kpi)
    parser_json.upload_file(param_edge.path_state_current + "state_prediction.json", param_edge.state_prediction)
