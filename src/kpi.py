#---------------------------------------------
from param import param_hu
from src import parser_json
from pymongo import MongoClient

import datetime;
import json
import sys
import hashlib
import argparse
import time
import pymongo


def format_state_kpi():
    # Load kpi state file
    param_hu.state_kpi = parser_json.load_data_from_file(param_hu.path_state_kpi)

    # Add values
    param_hu.state_kpi["timestamp"] = datetime.datetime.now().timestamp()

    param_hu.state_kpi["uplink_throughput_Mbs"] = param_hu.state_py["lidar_1"]["throughput"]["value"]

    param_hu.state_kpi["uplink_bandwidth_Mbs"] = param_hu.state_perf["local_cloud"]["bandwidth"]["value"]
    param_hu.state_kpi["downlink_bandwidth_Mbs"] = param_hu.state_perf["cloud_local"]["bandwidth"]["value"]

    param_hu.state_kpi["uplink_cloud_end_to_end_latency_ms"] = param_hu.state_perf["local_cloud"]["latency"]["value"]
    param_hu.state_kpi["downlink_cloud_end_to_end_latency_ms"] = param_hu.state_perf["cloud_local"]["latency"]["value"]

    param_hu.state_kpi["uplink_reliability_%"] = param_hu.state_perf["local_cloud"]["reliability"]["value"]
    param_hu.state_kpi["downlink_reliability_%"] = param_hu.state_perf["cloud_local"]["reliability"]["value"]

    param_hu.state_kpi["mobility_interruption_time_s"] = param_hu.state_perf["local_cloud"]["interruption"]["value"]
    param_hu.state_kpi["time_for_service_warning_ms"] = param_hu.state_perf["end_to_end"]["time_total"]

    # Upload kpi state file
    parser_json.upload_file(param_hu.path_state_kpi, param_hu.state_kpi)

def get_collection(url, database_name, collection_name, username, password):
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    server_url = ""
    if username and password:
        server_url = "mongodb://" + username + ":" + password + "@" + url
    else:
        server_url = "mongodb://" + url

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(server_url)

    # Create the database for our example (we will use the same database throughout the tutorial
    database = client[database_name]
    #print(database[collection_name])

    return database[collection_name]

def send_kpi_to_mongodb():
    url = "10.17.7.35:27017"
    database_name = "20221107_5gmed_UC3_P2"
    collection_name = "ServiceKpis"
    username = ""
    password = ""

    try:
        # Get collection pointer
        collection = get_collection(url, database_name, collection_name,  username, password)

        # Insert kpi json into collection
        #parsed = json.loads(param_hu.state_kpi)
        collection.insert_one(param_hu.state_kpi)
    except:
        print("[\033[1;31merror\033[0m] Failed to send KPIs")
