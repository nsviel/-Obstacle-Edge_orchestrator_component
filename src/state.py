#---------------------------------------------
from param import param_hu
from src import connection
from src import parser_json


def load_configuration():
    load_json_file()
    init_state_py()
    init_state_perf()
    load_config_file()
    upload_state()

def load_json_file():
    param_hu.state_hu = parser_json.load_data_from_file(param_hu.path_state_hu)
    param_hu.state_py = parser_json.load_data_from_file(param_hu.path_state_py)
    param_hu.state_perf = parser_json.load_data_from_file(param_hu.path_state_perf)

def init_state_py():
    param_hu.state_hu["self"]["ip"] = connection.get_ip_adress()
    param_hu.state_hu["self"]["sock_server_l1_source"] = "lidar_1"
    param_hu.state_hu["self"]["sock_server_l2_source"] = "lidar_2"
    param_hu.state_hu["self"]["nb_thread"] = 0
    param_hu.state_hu["data"]["nb_frame"] = 0
    param_hu.state_hu["data"]["nb_prediction"] = 0

    param_hu.state_hu["ai"]["http_connected"] = False
    param_hu.state_hu["velodium"]["sock_connected"] = False
    param_hu.state_hu["pywardium"]["http_connected"] = False
    param_hu.state_hu["pywardium"]["sock_l1_connected"] = False
    param_hu.state_hu["pywardium"]["sock_l2_connected"] = False
    param_hu.state_hu["velodium"]["sock_connected"] = False
    param_hu.state_hu["velodium"]["http_connected"] = False
    param_hu.state_hu["valeo"]["http_connected"] = False
    param_hu.state_hu["edge"]["http_connected"] = False
    param_hu.state_hu["edge"]["sock_connected"] = False
    param_hu.state_hu["sncf"]["broker_connected"] = False

def init_state_perf():
    param_hu.state_perf["local_cloud"]["time"] = 0
    param_hu.state_perf["local_cloud"]["bandwidth"]["value"] = 0
    param_hu.state_perf["local_cloud"]["bandwidth"]["min"] = 0
    param_hu.state_perf["local_cloud"]["bandwidth"]["max"] = 0
    param_hu.state_perf["local_cloud"]["bandwidth"]["mean"] = 0
    param_hu.state_perf["local_cloud"]["latency"]["value"] = 0
    param_hu.state_perf["local_cloud"]["latency"]["min"] = 0
    param_hu.state_perf["local_cloud"]["latency"]["max"] = 0
    param_hu.state_perf["local_cloud"]["latency"]["mean"] = 0
    param_hu.state_perf["local_cloud"]["jitter"]["value"] = 0
    param_hu.state_perf["local_cloud"]["jitter"]["min"] = 0
    param_hu.state_perf["local_cloud"]["jitter"]["max"] = 0
    param_hu.state_perf["local_cloud"]["jitter"]["mean"] = 0
    param_hu.state_perf["local_cloud"]["reliability"]["value"] = 0
    param_hu.state_perf["local_cloud"]["reliability"]["min"] = 0
    param_hu.state_perf["local_cloud"]["reliability"]["max"] = 0
    param_hu.state_perf["local_cloud"]["reliability"]["mean"] = 0
    param_hu.state_perf["local_cloud"]["interruption"]["value"] = 0
    param_hu.state_perf["local_cloud"]["interruption"]["min"] = 0
    param_hu.state_perf["local_cloud"]["interruption"]["max"] = 0
    param_hu.state_perf["local_cloud"]["interruption"]["mean"] = 0

    param_hu.state_perf["cloud_local"]["time"] = 0
    param_hu.state_perf["cloud_local"]["bandwidth"]["value"] = 0
    param_hu.state_perf["cloud_local"]["bandwidth"]["min"] = 0
    param_hu.state_perf["cloud_local"]["bandwidth"]["max"] = 0
    param_hu.state_perf["cloud_local"]["bandwidth"]["mean"] = 0
    param_hu.state_perf["cloud_local"]["latency"]["value"] = 0
    param_hu.state_perf["cloud_local"]["latency"]["min"] = 0
    param_hu.state_perf["cloud_local"]["latency"]["max"] = 0
    param_hu.state_perf["cloud_local"]["latency"]["mean"] = 0
    param_hu.state_perf["cloud_local"]["jitter"]["value"] = 0
    param_hu.state_perf["cloud_local"]["jitter"]["min"] = 0
    param_hu.state_perf["cloud_local"]["jitter"]["max"] = 0
    param_hu.state_perf["cloud_local"]["jitter"]["mean"] = 0
    param_hu.state_perf["cloud_local"]["reliability"]["value"] = 0
    param_hu.state_perf["cloud_local"]["reliability"]["min"] = 0
    param_hu.state_perf["cloud_local"]["reliability"]["max"] = 0
    param_hu.state_perf["cloud_local"]["reliability"]["mean"] = 0

def load_config_file():
    config = parser_json.load_data_from_file(param_hu.path_config)
    param_hu.state_hu["self"]["country"] = config["self"]["country"]
    param_hu.state_hu["self"]["edge_id"] = config["self"]["edge_id"]
    param_hu.state_hu["self"]["sock_server_l1_port"] = config["self"]["sock_server_l1_port"]
    param_hu.state_hu["self"]["sock_server_l2_port"] = config["self"]["sock_server_l2_port"]
    param_hu.state_hu["self"]["http_server_port"] = config["self"]["http_server_port"]
    param_hu.state_hu["self"]["iperf_port"] = config["self"]["iperf_port"]

    param_hu.state_hu["pywardium"]["ip"] = config["pywardium"]["ip"]
    param_hu.state_hu["pywardium"]["http_server_port"] = config["pywardium"]["http_server_port"]
    param_hu.state_hu["pywardium"]["iperf_port"] = config["pywardium"]["iperf_port"]

    param_hu.state_hu["controlium"]["ip"] = config["controlium"]["ip"]
    param_hu.state_hu["controlium"]["sock_server_l1_port"] = config["controlium"]["sock_server_l1_port"]
    param_hu.state_hu["controlium"]["sock_server_l2_port"] = config["controlium"]["sock_server_l2_port"]

    param_hu.state_hu["sncf"]["broker_ip"] = config["sncf"]["broker_ip"]
    param_hu.state_hu["sncf"]["broker_port"] = config["sncf"]["broker_port"]
    param_hu.state_hu["sncf"]["mqtt_client"] = config["sncf"]["mqtt_client"]
    param_hu.state_hu["sncf"]["mqtt_topic"] = config["sncf"]["mqtt_topic"]

    param_hu.state_hu["velodium"]["ip"] = config["velodium"]["ip"]
    param_hu.state_hu["velodium"]["sock_server_port"] = config["velodium"]["sock_server_port"]
    param_hu.state_hu["velodium"]["http_server_port"] = config["velodium"]["http_server_port"]

    param_hu.state_hu["ai"]["ip"] = config["ai"]["ip"]
    param_hu.state_hu["ai"]["http_server_port"] = config["ai"]["http_server_port"]

    param_hu.state_hu["valeo"]["ip"] = config["valeo"]["ip"]
    param_hu.state_hu["edge"]["ip"] = config["edge"]["ip"]

def upload_state():
    parser_json.upload_file(param_hu.path_state_hu, param_hu.state_hu)
    parser_json.upload_file(param_hu.path_state_perf, param_hu.state_perf)
