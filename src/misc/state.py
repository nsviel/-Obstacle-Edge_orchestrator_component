#---------------------------------------------
from src.param import param_hu
from src.misc import connection
from src.misc import parser_json
from src.misc import terminal


def load_configuration():
    load_json_file()
    init_state_py()
    init_state_perf()
    load_config_file()
    upload_state()
    terminal.addLog("#", "Configuration loaded")

def load_json_file():
    param_hu.state_hu = parser_json.load_state(param_hu.path_state_hu)
    param_hu.state_py = parser_json.load_state(param_hu.path_state_py)
    param_hu.state_perf = parser_json.load_state(param_hu.path_state_perf)
    param_hu.state_kpi = parser_json.load_state(param_hu.path_state_kpi)

def init_state_py():
    param_hu.state_hu["self"]["ip"] = connection.get_ip_adress()
    param_hu.state_hu["self"]["lidar_main"] = "lidar_1"
    param_hu.state_hu["self"]["nb_thread"] = 0
    param_hu.state_hu["data"]["nb_frame"] = 0
    param_hu.state_hu["data"]["nb_prediction"] = 0

    param_hu.state_hu["component_ai"]["http_connected"] = False
    param_hu.state_hu["component_process"]["sock_connected"] = False
    param_hu.state_hu["module_capture"]["http_connected"] = False
    param_hu.state_hu["module_capture"]["sock_l1_connected"] = False
    param_hu.state_hu["module_capture"]["sock_l2_connected"] = False
    param_hu.state_hu["component_process"]["sock_connected"] = False
    param_hu.state_hu["component_process"]["http_connected"] = False
    param_hu.state_hu["cloud_car"]["http_connected"] = False
    param_hu.state_hu["edge_next"]["http_connected"] = False
    param_hu.state_hu["edge_next"]["sock_connected"] = False
    param_hu.state_hu["train_operator"]["broker_connected"] = False

def init_state_perf():
    param_hu.state_perf["mongo"]["connected"] = False
    param_hu.state_kpi["ID"] = 0

    param_hu.state_perf["local_cloud"]["timestamp"] = 0
    param_hu.state_perf["local_cloud"]["throughput"]["value"] = 0
    param_hu.state_perf["local_cloud"]["throughput"]["min"] = 0
    param_hu.state_perf["local_cloud"]["throughput"]["max"] = 0
    param_hu.state_perf["local_cloud"]["throughput"]["mean"] = 0
    param_hu.state_perf["local_cloud"]["latency"]["value"] = 0
    param_hu.state_perf["local_cloud"]["latency"]["min"] = 0
    param_hu.state_perf["local_cloud"]["latency"]["max"] = 0
    param_hu.state_perf["local_cloud"]["latency"]["mean"] = 0
    param_hu.state_perf["local_cloud"]["reliability"]["value"] = 0
    param_hu.state_perf["local_cloud"]["reliability"]["min"] = 0
    param_hu.state_perf["local_cloud"]["reliability"]["max"] = 0
    param_hu.state_perf["local_cloud"]["reliability"]["mean"] = 0
    param_hu.state_perf["local_cloud"]["interruption"]["value"] = 0
    param_hu.state_perf["local_cloud"]["interruption"]["min"] = 0
    param_hu.state_perf["local_cloud"]["interruption"]["max"] = 0
    param_hu.state_perf["local_cloud"]["interruption"]["mean"] = 0

    param_hu.state_perf["cloud_local"]["timestamp"] = 0
    param_hu.state_perf["cloud_local"]["latency"]["value"] = 0
    param_hu.state_perf["cloud_local"]["latency"]["min"] = 0
    param_hu.state_perf["cloud_local"]["latency"]["max"] = 0
    param_hu.state_perf["cloud_local"]["latency"]["mean"] = 0
    param_hu.state_perf["cloud_local"]["reliability"]["value"] = 0
    param_hu.state_perf["cloud_local"]["reliability"]["min"] = 0
    param_hu.state_perf["cloud_local"]["reliability"]["max"] = 0
    param_hu.state_perf["cloud_local"]["reliability"]["mean"] = 0

    param_hu.state_perf["end_to_end"]["time_slam"] = 0
    param_hu.state_perf["end_to_end"]["time_ai"] = 0
    param_hu.state_perf["end_to_end"]["time_total"] = 0

def load_config_file():
    config = parser_json.load_data_from_file(param_hu.path_config)
    param_hu.state_hu["self"]["country"] = config["self"]["country"]
    param_hu.state_hu["self"]["edge_id"] = config["self"]["edge_id"]
    param_hu.state_hu["self"]["sock_server_l1_port"] = config["self"]["sock_server_l1_port"]
    param_hu.state_hu["self"]["sock_server_l2_port"] = config["self"]["sock_server_l2_port"]
    param_hu.state_hu["self"]["http_server_port"] = config["self"]["http_server_port"]
    param_hu.tic_connection = config["self"]["tic_connection"]
    param_hu.tic_network = config["self"]["tic_network"]

    param_hu.state_hu["module_capture"]["ip"] = config["module_capture"]["ip"]
    param_hu.state_hu["module_capture"]["http_server_port"] = config["module_capture"]["http_server_port"]

    param_hu.state_hu["module_interface"]["ip"] = config["module_interface"]["ip"]
    param_hu.state_hu["module_interface"]["sock_server_l1_port"] = config["module_interface"]["sock_server_l1_port"]
    param_hu.state_hu["module_interface"]["sock_server_l2_port"] = config["module_interface"]["sock_server_l2_port"]

    param_hu.state_hu["train_operator"]["broker_ip"] = config["train_operator"]["broker_ip"]
    param_hu.state_hu["train_operator"]["broker_port"] = config["train_operator"]["broker_port"]
    param_hu.state_hu["train_operator"]["mqtt_client"] = config["train_operator"]["mqtt_client"]
    param_hu.state_hu["train_operator"]["mqtt_topic"] = config["train_operator"]["mqtt_topic"]

    param_hu.state_hu["component_process"]["ip"] = config["component_process"]["ip"]
    param_hu.state_hu["component_process"]["sock_server_port"] = config["component_process"]["sock_server_port"]
    param_hu.state_hu["component_process"]["http_server_port"] = config["component_process"]["http_server_port"]

    param_hu.state_hu["component_ai"]["ip"] = config["component_ai"]["ip"]
    param_hu.state_hu["component_ai"]["http_server_port"] = config["component_ai"]["http_server_port"]

    param_hu.state_hu["cloud_car"]["ip"] = config["cloud_car"]["ip"]
    param_hu.state_hu["edge_next"]["ip"] = config["edge_next"]["ip"]

    param_hu.state_perf["mongo"]["ip"] = config["perf"]["mongo_ip"]
    param_hu.state_perf["mongo"]["port"] = config["perf"]["mongo_port"]
    param_hu.state_perf["mongo"]["database"] = config["perf"]["mongo_database"]
    param_hu.state_perf["mongo"]["collection"] = config["perf"]["mongo_collection"]
    param_hu.state_perf["mongo"]["username"] = config["perf"]["mongo_username"]
    param_hu.state_perf["mongo"]["password"] = config["perf"]["mongo_password"]
    param_hu.state_perf["mongo"]["nb_data"] = config["perf"]["mongo_nb_data"]

def upload_state():
    parser_json.upload_file(param_hu.path_state_hu, param_hu.state_hu)
    parser_json.upload_file(param_hu.path_state_perf, param_hu.state_perf)
    parser_json.upload_file(param_hu.path_state_kpi, param_hu.state_kpi)
