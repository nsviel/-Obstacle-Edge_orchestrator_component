#---------------------------------------------
from src.param import param_edge
from src.utils import parser_json
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from collections import deque

import datetime;
import json
import sys
import hashlib
import argparse
import time
import pymongo
import copy

class RollingMean:
    def __init__(self, window_size):
        self.window = deque(maxlen=window_size)  # Circular buffer to store last n values
        self.sum = 0  # Sum of values in the window
        self.mean = 0  # Current mean value

    def add_value(self, value):
        # Update sum by subtracting the oldest value and adding the new value
        if len(self.window) == self.window.maxlen:
            self.sum -= self.window[0]
        self.sum += value
        # Add new value to the window
        self.window.append(value)
        # Update mean
        self.mean = self.sum / len(self.window)

    def get_mean(self):
        return self.mean


latency_edge_to_ground_mean = RollingMean(20)
latency_ground_to_edge_mean = RollingMean(20)
uplink_data_rate_mean = RollingMean(20)
def format_state_kpi():
    latency_edge_to_ground_mean.add_value(float(param_edge.state_network["edge_to_ground"]["latency"]["value"]))
    latency_ground_to_edge_mean.add_value(float(param_edge.state_network["ground_to_edge"]["latency"]["value"]))
    uplink_data_rate_mean.add_value(float(param_edge.state_ground["lidar_1"]["throughput"]["value"]))

    main_source = param_edge.state_edge["hub"]["socket"]["lidar_main"]
    timestamp = datetime.datetime.now().timestamp()

    kpis = {
        "timestamp": datetime.datetime.utcfromtimestamp(timestamp),
        "P2_uplink_data_rate_Mbs": uplink_data_rate_mean.get_mean(),

        "P2_uplink_cloud_end_to_end_latency_ms": latency_ground_to_edge_mean.get_mean(),
        "P2_downlink_cloud_end_to_end_latency_ms": latency_edge_to_ground_mean.get_mean(),

        "P2_uplink_reliability_%": float(param_edge.state_network["ground_to_edge"]["reliability"]["value"]),
        "P2_downlink_reliability_%": float(param_edge.state_network["edge_to_ground"]["reliability"]["value"]),

        "P2_time_mobility_interruption_s": float(param_edge.state_network["ground_to_edge"]["interruption"]["value"]),
        "P2_time_service_warning_ms": float(param_edge.state_network["time"]["total"]),
        "ID": param_edge.state_kpi["ID"] + 1,

        "service": "P2"
    }
    return kpis

def send_kpi_to_mongodb():
    ip = param_edge.state_network["mongodb"]["ip"]
    port = param_edge.state_network["mongodb"]["port"]
    database_name = param_edge.state_network["mongodb"]["database"]
    collection_name = param_edge.state_network["mongodb"]["collection"]
    username = param_edge.state_network["mongodb"]["username"]
    password = param_edge.state_network["mongodb"]["password"]
    nb_kept_data = param_edge.state_network["mongodb"]["nb_data"]

    kpis = format_state_kpi()

    try:
        # Get collection pointer
        url = ip + ":" + str(port)
        collection = get_collection(url, database_name, collection_name, username, password)
        collection.insert_one(kpis)

        # Update connection info
        param_edge.state_network["mongodb"]["connected"] = True
    except:
        param_edge.state_network["mongodb"]["connected"] = False
        pass

def get_collection(url, database_name, collection_name, username, password):
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    if username and password:
        server_url = "mongodb://" + username + ":" + password + "@" + url
    else:
        server_url = "mongodb://" + url + "/"

    # Create a connection using MongoClient
    client = MongoClient(server_url, connectTimeoutMS=1000, serverSelectionTimeoutMS=1000, waitQueueTimeoutMS=1000)

    # Create the database
    database = client[database_name]

    return database[collection_name]

# Delete data older than the day
def control_collection_old_data(collection, nb_kept_data):
    umber_of_days = 1
    cutoff_date = datetime.datetime.utcnow() - datetime.timedelta(days=number_of_days)
    collection.delete_many({"orderExpDate": {"$lt": cutoff_date}})
