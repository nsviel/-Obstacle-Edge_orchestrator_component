#---------------------------------------------
from src.param import param_edge
from src.connection.HTTPS.client import https_client_get
from src.network import network_ping
from src.network import network_module
from src.network import network_mongo
from src.utils import parser_json
from src.base import daemon

import multiprocessing as mp
import threading
import time


class Network(daemon.Daemon):
    def __init__(self):
        self.name = "Network performance";
        self.run_sleep = 0.5;
        self.list_reliability = []
        self.list_latency = []
        self.list_interruption = []

    def thread_function(self):
        # Update from py perf state
        self.update_perf_from_ground()

        # Ping
        network_ping.compute_ping(self)

        # System time retrieving
        network_module.ask_for_time()

        # Make mongo stuff
        network_mongo.format_state_kpi()
        network_mongo.send_kpi_to_mongodb()

        # Update state file and sleep one second
        parser_json.upload_file(param_edge.path_state_current + "state_network.json", param_edge.state_network)

    def update_perf_from_ground(self):
        ground_state_network = https_client_get.get_state("network")
        if(ground_state_network == None):
            return

        param_edge.state_network["local_cloud"]["timestamp"] = ground_state_network["local_cloud"]["timestamp"]

        param_edge.state_network["local_cloud"]["throughput"]["value"] = ground_state_network["local_cloud"]["throughput"]["value"]
        param_edge.state_network["local_cloud"]["throughput"]["min"] = ground_state_network["local_cloud"]["throughput"]["min"]
        param_edge.state_network["local_cloud"]["throughput"]["max"] = ground_state_network["local_cloud"]["throughput"]["max"]
        param_edge.state_network["local_cloud"]["throughput"]["mean"] = ground_state_network["local_cloud"]["throughput"]["mean"]

        param_edge.state_network["local_cloud"]["reliability"]["value"] = ground_state_network["local_cloud"]["reliability"]["value"]
        param_edge.state_network["local_cloud"]["reliability"]["min"] = ground_state_network["local_cloud"]["reliability"]["min"]
        param_edge.state_network["local_cloud"]["reliability"]["max"] = ground_state_network["local_cloud"]["reliability"]["max"]
        param_edge.state_network["local_cloud"]["reliability"]["mean"] = ground_state_network["local_cloud"]["reliability"]["mean"]

        param_edge.state_network["local_cloud"]["interruption"]["value"] = ground_state_network["local_cloud"]["interruption"]["value"]
        param_edge.state_network["local_cloud"]["interruption"]["min"] = ground_state_network["local_cloud"]["interruption"]["min"]
        param_edge.state_network["local_cloud"]["interruption"]["max"] = ground_state_network["local_cloud"]["interruption"]["max"]
        param_edge.state_network["local_cloud"]["interruption"]["mean"] = ground_state_network["local_cloud"]["interruption"]["mean"]

        param_edge.state_network["local_cloud"]["latency"]["value"] = ground_state_network["local_cloud"]["latency"]["value"]
        param_edge.state_network["local_cloud"]["latency"]["min"] = ground_state_network["local_cloud"]["latency"]["min"]
        param_edge.state_network["local_cloud"]["latency"]["max"] = ground_state_network["local_cloud"]["latency"]["max"]
        param_edge.state_network["local_cloud"]["latency"]["mean"] = ground_state_network["local_cloud"]["latency"]["mean"]
