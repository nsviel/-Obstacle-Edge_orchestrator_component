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
    def thread_function(self):
        # Update from py perf state
        self.update_perf_from_py()

        # Ping
        network_ping.compute_ping(self.list_latency, self.list_reliability)

        # System time retrieving
        network_module.ask_for_time()

        # Make mongo stuff
        network_mongo.format_state_kpi()
        network_mongo.send_kpi_to_mongodb()

        # Update state file and sleep one second
        parser_json.upload_file(param_edge.path_state_current + "state_network.json", param_edge.state_network)

    def update_perf_from_py(self):
        capture_state_network = https_client_get.get_state_data("network")
        if(capture_state_network == None):
            return

        param_edge.state_network["local_cloud"]["timestamp"] = capture_state_network["local_cloud"]["timestamp"]

        param_edge.state_network["local_cloud"]["throughput"]["value"] = capture_state_network["local_cloud"]["throughput"]["value"]
        param_edge.state_network["local_cloud"]["throughput"]["min"] = capture_state_network["local_cloud"]["throughput"]["min"]
        param_edge.state_network["local_cloud"]["throughput"]["max"] = capture_state_network["local_cloud"]["throughput"]["max"]
        param_edge.state_network["local_cloud"]["throughput"]["mean"] = capture_state_network["local_cloud"]["throughput"]["mean"]

        param_edge.state_network["local_cloud"]["reliability"]["value"] = capture_state_network["local_cloud"]["reliability"]["value"]
        param_edge.state_network["local_cloud"]["reliability"]["min"] = capture_state_network["local_cloud"]["reliability"]["min"]
        param_edge.state_network["local_cloud"]["reliability"]["max"] = capture_state_network["local_cloud"]["reliability"]["max"]
        param_edge.state_network["local_cloud"]["reliability"]["mean"] = capture_state_network["local_cloud"]["reliability"]["mean"]

        param_edge.state_network["local_cloud"]["interruption"]["value"] = capture_state_network["local_cloud"]["interruption"]["value"]
        param_edge.state_network["local_cloud"]["interruption"]["min"] = capture_state_network["local_cloud"]["interruption"]["min"]
        param_edge.state_network["local_cloud"]["interruption"]["max"] = capture_state_network["local_cloud"]["interruption"]["max"]
        param_edge.state_network["local_cloud"]["interruption"]["mean"] = capture_state_network["local_cloud"]["interruption"]["mean"]

        param_edge.state_network["local_cloud"]["latency"]["value"] = capture_state_network["local_cloud"]["latency"]["value"]
        param_edge.state_network["local_cloud"]["latency"]["min"] = capture_state_network["local_cloud"]["latency"]["min"]
        param_edge.state_network["local_cloud"]["latency"]["max"] = capture_state_network["local_cloud"]["latency"]["max"]
        param_edge.state_network["local_cloud"]["latency"]["mean"] = capture_state_network["local_cloud"]["latency"]["mean"]

    name = "Network performance";
    run_sleep = 0.5;
    list_reliability = []
    list_latency = []
