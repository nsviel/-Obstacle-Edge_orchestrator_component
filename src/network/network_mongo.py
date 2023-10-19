#---------------------------------------------
from src.param import param_edge
from src.utils import parser_json
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

import datetime;
import json
import sys
import hashlib
import argparse
import time
import pymongo
import copy


def format_state_kpi():
    timestamp = datetime.datetime.now().timestamp()
    date =str(datetime.datetime.utcfromtimestamp(timestamp))
    param_edge.state_kpi["timestamp"] = date
    param_edge.state_kpi["uplink_data_rate_Mbs"] = param_edge.state_ground["lidar_1"]["throughput"]["value"]
    param_edge.state_kpi["uplink_cloud_end_to_end_latency_ms"] = param_edge.state_network["ground_to_edge"]["latency"]["value"]
    param_edge.state_kpi["downlink_cloud_end_to_end_latency_ms"] = param_edge.state_network["edge_to_ground"]["latency"]["value"]
    param_edge.state_kpi["uplink_reliability_%"] = param_edge.state_network["ground_to_edge"]["reliability"]["value"]
    param_edge.state_kpi["downlink_reliability_%"] = param_edge.state_network["edge_to_ground"]["reliability"]["value"]
    param_edge.state_kpi["time_mobility_interruption_s"] = param_edge.state_network["ground_to_edge"]["interruption"]["value"]
    param_edge.state_kpi["time_service_warning_ms"] = param_edge.state_network["time"]["total"]
    param_edge.state_kpi["ID"] = param_edge.state_kpi["ID"] + 1
    param_edge.state_kpi["service"] = "P2"

    #print(param_edge.state_kpi["uplink_reliability_%"]);

    kpis = {
        "timestamp": datetime.datetime.utcfromtimestamp(timestamp),
        "uplink_data_rate_Mbs": float(param_edge.state_ground["lidar_1"]["throughput"]["value"]),
        "uplink_cloud_end_to_end_latency_ms": float(param_edge.state_network["ground_to_edge"]["latency"]["value"]),

        "downlink_cloud_end_to_end_latency_ms": float(param_edge.state_network["edge_to_ground"]["latency"]["value"]),
        "uplink_reliability_%": float(param_edge.state_network["ground_to_edge"]["reliability"]["value"]),
        "downlink_reliability_%": float(param_edge.state_network["edge_to_ground"]["reliability"]["value"]),

        "time_mobility_interruption_s": float(param_edge.state_network["ground_to_edge"]["interruption"]["value"]),
        "time_service_warning_ms": float(param_edge.state_network["time"]["total"]),
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

        # Check for data number
        #control_collection_old_data(collection, nb_kept_data)

        # Insert kpi json into collection
        #kpi = copy.deepcopy(param_edge.state_kpi)
        #collection.insert_one(kpi)

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
