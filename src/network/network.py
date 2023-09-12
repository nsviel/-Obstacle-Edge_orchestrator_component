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

        param_edge.state_network["ground_to_edge"]["timestamp"] = ground_state_network["ground_to_edge"]["timestamp"]

        param_edge.state_network["ground_to_edge"]["throughput"]["value"] = ground_state_network["ground_to_edge"]["throughput"]["value"]
        param_edge.state_network["ground_to_edge"]["throughput"]["min"] = ground_state_network["ground_to_edge"]["throughput"]["min"]
        param_edge.state_network["ground_to_edge"]["throughput"]["max"] = ground_state_network["ground_to_edge"]["throughput"]["max"]
        param_edge.state_network["ground_to_edge"]["throughput"]["mean"] = ground_state_network["ground_to_edge"]["throughput"]["mean"]

        param_edge.state_network["ground_to_edge"]["reliability"]["value"] = ground_state_network["ground_to_edge"]["reliability"]["value"]
        param_edge.state_network["ground_to_edge"]["reliability"]["min"] = ground_state_network["ground_to_edge"]["reliability"]["min"]
        param_edge.state_network["ground_to_edge"]["reliability"]["max"] = ground_state_network["ground_to_edge"]["reliability"]["max"]
        param_edge.state_network["ground_to_edge"]["reliability"]["mean"] = ground_state_network["ground_to_edge"]["reliability"]["mean"]

        param_edge.state_network["ground_to_edge"]["interruption"]["value"] = ground_state_network["ground_to_edge"]["interruption"]["value"]
        param_edge.state_network["ground_to_edge"]["interruption"]["min"] = ground_state_network["ground_to_edge"]["interruption"]["min"]
        param_edge.state_network["ground_to_edge"]["interruption"]["max"] = ground_state_network["ground_to_edge"]["interruption"]["max"]
        param_edge.state_network["ground_to_edge"]["interruption"]["mean"] = ground_state_network["ground_to_edge"]["interruption"]["mean"]

        param_edge.state_network["ground_to_edge"]["latency"]["value"] = ground_state_network["ground_to_edge"]["latency"]["value"]
        param_edge.state_network["ground_to_edge"]["latency"]["min"] = ground_state_network["ground_to_edge"]["latency"]["min"]
        param_edge.state_network["ground_to_edge"]["latency"]["max"] = ground_state_network["ground_to_edge"]["latency"]["max"]
        param_edge.state_network["ground_to_edge"]["latency"]["mean"] = ground_state_network["ground_to_edge"]["latency"]["mean"]
