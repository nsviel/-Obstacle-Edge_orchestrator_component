#---------------------------------------------
from src.param import param_edge
from src.connection import connection
from src.utils import parser_json
from src.utils import terminal


def load_configuration():
    load_json_file()
    init_state_capture()
    init_state_network()
    load_config_file()
    upload_state()
    terminal.addLog("#", "Configuration loaded")

def load_json_file():
    param_edge.state_edge_1 = parser_json.load_state(param_edge.path_state_edge_1)
    param_edge.state_capture = parser_json.load_state(param_edge.path_state_capture)
    param_edge.state_network = parser_json.load_state(param_edge.path_state_network)
    param_edge.state_kpi = parser_json.load_state(param_edge.path_state_kpi)

def init_state_capture():
    param_edge.state_edge_1["self"]["ip"] = connection.get_ip_adress()
    param_edge.state_edge_1["self"]["lidar_main"] = "lidar_1"
    param_edge.state_edge_1["self"]["nb_thread"] = 0
    param_edge.state_edge_1["data"]["nb_frame"] = 0
    param_edge.state_edge_1["data"]["nb_prediction"] = 0

    param_edge.state_edge_1["component_ai"]["http_connected"] = False
    param_edge.state_edge_1["component_process"]["sock_connected"] = False
    param_edge.state_edge_1["module_capture"]["http_connected"] = False
    param_edge.state_edge_1["module_capture"]["sock_l1_connected"] = False
    param_edge.state_edge_1["module_capture"]["sock_l2_connected"] = False
    param_edge.state_edge_1["component_process"]["sock_connected"] = False
    param_edge.state_edge_1["component_process"]["http_connected"] = False
    param_edge.state_edge_1["cloud_car"]["http_connected"] = False
    param_edge.state_edge_1["edge_next"]["http_connected"] = False
    param_edge.state_edge_1["edge_next"]["sock_connected"] = False
    param_edge.state_edge_1["train_operator"]["broker_connected"] = False

def init_state_network():
    param_edge.state_network["mongo"]["connected"] = False
    param_edge.state_kpi["ID"] = 0

    param_edge.state_network["local_cloud"]["timestamp"] = 0
    param_edge.state_network["local_cloud"]["throughput"]["value"] = 0
    param_edge.state_network["local_cloud"]["throughput"]["min"] = 0
    param_edge.state_network["local_cloud"]["throughput"]["max"] = 0
    param_edge.state_network["local_cloud"]["throughput"]["mean"] = 0
    param_edge.state_network["local_cloud"]["latency"]["value"] = 0
    param_edge.state_network["local_cloud"]["latency"]["min"] = 0
    param_edge.state_network["local_cloud"]["latency"]["max"] = 0
    param_edge.state_network["local_cloud"]["latency"]["mean"] = 0
    param_edge.state_network["local_cloud"]["reliability"]["value"] = 0
    param_edge.state_network["local_cloud"]["reliability"]["min"] = 0
    param_edge.state_network["local_cloud"]["reliability"]["max"] = 0
    param_edge.state_network["local_cloud"]["reliability"]["mean"] = 0
    param_edge.state_network["local_cloud"]["interruption"]["value"] = 0
    param_edge.state_network["local_cloud"]["interruption"]["min"] = 0
    param_edge.state_network["local_cloud"]["interruption"]["max"] = 0
    param_edge.state_network["local_cloud"]["interruption"]["mean"] = 0

    param_edge.state_network["cloud_local"]["timestamp"] = 0
    param_edge.state_network["cloud_local"]["latency"]["value"] = 0
    param_edge.state_network["cloud_local"]["latency"]["min"] = 0
    param_edge.state_network["cloud_local"]["latency"]["max"] = 0
    param_edge.state_network["cloud_local"]["latency"]["mean"] = 0
    param_edge.state_network["cloud_local"]["reliability"]["value"] = 0
    param_edge.state_network["cloud_local"]["reliability"]["min"] = 0
    param_edge.state_network["cloud_local"]["reliability"]["max"] = 0
    param_edge.state_network["cloud_local"]["reliability"]["mean"] = 0

    param_edge.state_network["end_to_end"]["time_slam"] = 0
    param_edge.state_network["end_to_end"]["time_ai"] = 0
    param_edge.state_network["end_to_end"]["time_total"] = 0

def load_config_file():
    config = parser_json.load_data_from_file(param_edge.path_config)
    param_edge.state_edge_1["self"]["country"] = config["self"]["country"]
    param_edge.state_edge_1["self"]["edge_id"] = config["self"]["edge_id"]
    param_edge.state_edge_1["self"]["sock_server_l1_port"] = config["self"]["sock_server_l1_port"]
    param_edge.state_edge_1["self"]["sock_server_l2_port"] = config["self"]["sock_server_l2_port"]
    param_edge.state_edge_1["self"]["http_server_port"] = config["self"]["http_server_port"]
    param_edge.tic_connection = config["self"]["tic_connection"]
    param_edge.tic_network = config["self"]["tic_network"]

    param_edge.state_edge_1["module_capture"]["ip"] = config["module_capture"]["ip"]
    param_edge.state_edge_1["module_capture"]["http_server_port"] = config["module_capture"]["http_server_port"]

    param_edge.state_edge_1["module_interface"]["ip"] = config["module_interface"]["ip"]
    param_edge.state_edge_1["module_interface"]["sock_server_l1_port"] = config["module_interface"]["sock_server_l1_port"]
    param_edge.state_edge_1["module_interface"]["sock_server_l2_port"] = config["module_interface"]["sock_server_l2_port"]

    param_edge.state_edge_1["train_operator"]["broker_ip"] = config["train_operator"]["broker_ip"]
    param_edge.state_edge_1["train_operator"]["broker_port"] = config["train_operator"]["broker_port"]
    param_edge.state_edge_1["train_operator"]["mqtt_client"] = config["train_operator"]["mqtt_client"]
    param_edge.state_edge_1["train_operator"]["mqtt_topic"] = config["train_operator"]["mqtt_topic"]

    param_edge.state_edge_1["component_process"]["ip"] = config["component_process"]["ip"]
    param_edge.state_edge_1["component_process"]["sock_server_port"] = config["component_process"]["sock_server_port"]
    param_edge.state_edge_1["component_process"]["http_server_port"] = config["component_process"]["http_server_port"]

    param_edge.state_edge_1["component_ai"]["ip"] = config["component_ai"]["ip"]
    param_edge.state_edge_1["component_ai"]["http_server_port"] = config["component_ai"]["http_server_port"]

    param_edge.state_edge_1["cloud_car"]["ip"] = config["cloud_car"]["ip"]
    param_edge.state_edge_1["edge_next"]["ip"] = config["edge_next"]["ip"]

    param_edge.state_network["mongo"]["ip"] = config["network"]["mongo_ip"]
    param_edge.state_network["mongo"]["port"] = config["network"]["mongo_port"]
    param_edge.state_network["mongo"]["database"] = config["network"]["mongo_database"]
    param_edge.state_network["mongo"]["collection"] = config["network"]["mongo_collection"]
    param_edge.state_network["mongo"]["username"] = config["network"]["mongo_username"]
    param_edge.state_network["mongo"]["password"] = config["network"]["mongo_password"]
    param_edge.state_network["mongo"]["nb_data"] = config["network"]["mongo_nb_data"]

def upload_state():
    parser_json.upload_file(param_edge.path_state_edge_1, param_edge.state_edge_1)
    parser_json.upload_file(param_edge.path_state_network, param_edge.state_network)
    parser_json.upload_file(param_edge.path_state_kpi, param_edge.state_kpi)
