#---------------------------------------------
from src.param import param_edge
from src.misc import parser_json
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

import datetime;
import json
import sys
import hashlib
import argparse
import time
import pymongo


def format_state_kpi():
    param_edge.state_kpi = parser_json.load_state(param_edge.path_state_kpi)

    param_edge.state_kpi["timestamp"] = datetime.datetime.now().timestamp()
    param_edge.state_kpi["uplink_throughput_Mbs"] = param_edge.state_capture["lidar_1"]["throughput"]["value"]
    param_edge.state_kpi["uplink_cloud_end_to_end_latency_ms"] = param_edge.state_network["local_cloud"]["latency"]["value"]
    param_edge.state_kpi["downlink_cloud_end_to_end_latency_ms"] = param_edge.state_network["cloud_local"]["latency"]["value"]
    param_edge.state_kpi["uplink_reliability_%"] = param_edge.state_network["local_cloud"]["reliability"]["value"]
    param_edge.state_kpi["downlink_reliability_%"] = param_edge.state_network["cloud_local"]["reliability"]["value"]
    param_edge.state_kpi["mobility_interruption_time_s"] = param_edge.state_network["local_cloud"]["interruption"]["value"]
    param_edge.state_kpi["time_for_service_warning_ms"] = param_edge.state_network["end_to_end"]["time_total"]
    param_edge.state_kpi["ID"] = param_edge.state_kpi["ID"] + 1

    parser_json.upload_file(param_edge.path_state_kpi, param_edge.state_kpi)

def send_kpi_to_mongodb():
    ip = param_edge.state_network["mongo"]["ip"]
    port = param_edge.state_network["mongo"]["port"]
    database_name = param_edge.state_network["mongo"]["database"]
    collection_name = param_edge.state_network["mongo"]["collection"]
    username = param_edge.state_network["mongo"]["username"]
    password = param_edge.state_network["mongo"]["password"]
    nb_kept_data = param_edge.state_network["mongo"]["nb_data"]

    #database_name = "20221107_5gmed_UC3_P2"
    #collection_name = "ServiceKpis"

    try:
        # Get collection pointer
        url = ip + ":" + str(port)
        collection = get_collection(url, database_name, collection_name, username, password)

        # Check for data number
        control_collection_nbData(collection, nb_kept_data)

        # Insert kpi json into collection
        collection.insert_one(param_edge.state_kpi)

        # Update connection info
        param_edge.state_network["mongo"]["connected"] = True
    except:
        param_edge.state_network["mongo"]["connected"] = False
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

def control_collection_nbData(collection, nb_kept_data):
    if(param_edge.state_kpi["ID"] > nb_kept_data):
        to_supress = { "ID": param_edge.state_kpi["ID"] - nb_kept_data }
        collection.delete_one(to_supress)