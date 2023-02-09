#---------------------------------------------
from src.param import param_hu
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
    param_hu.state_kpi = parser_json.load_state(param_hu.path_state_kpi)

    param_hu.state_kpi["timestamp"] = datetime.datetime.now().timestamp()
    param_hu.state_kpi["uplink_throughput_Mbs"] = param_hu.state_py["lidar_1"]["throughput"]["value"]
    param_hu.state_kpi["uplink_cloud_end_to_end_latency_ms"] = param_hu.state_perf["local_cloud"]["latency"]["value"]
    param_hu.state_kpi["downlink_cloud_end_to_end_latency_ms"] = param_hu.state_perf["cloud_local"]["latency"]["value"]
    param_hu.state_kpi["uplink_reliability_%"] = param_hu.state_perf["local_cloud"]["reliability"]["value"]
    param_hu.state_kpi["downlink_reliability_%"] = param_hu.state_perf["cloud_local"]["reliability"]["value"]
    param_hu.state_kpi["mobility_interruption_time_s"] = param_hu.state_perf["local_cloud"]["interruption"]["value"]
    param_hu.state_kpi["time_for_service_warning_ms"] = param_hu.state_perf["end_to_end"]["time_total"]
    param_hu.state_kpi["ID"] = param_hu.state_kpi["ID"] + 1

    parser_json.upload_file(param_hu.path_state_kpi, param_hu.state_kpi)

def send_kpi_to_mongodb():
    ip = param_hu.state_perf["mongo"]["ip"]
    port = param_hu.state_perf["mongo"]["port"]
    database_name = param_hu.state_perf["mongo"]["database"]
    collection_name = param_hu.state_perf["mongo"]["collection"]
    username = param_hu.state_perf["mongo"]["username"]
    password = param_hu.state_perf["mongo"]["password"]
    nb_kept_data = param_hu.state_perf["mongo"]["nb_data"]

    #database_name = "20221107_5gmed_UC3_P2"
    #collection_name = "ServiceKpis"

    try:
        # Get collection pointer
        url = ip + ":" + str(port)
        collection = get_collection(url, database_name, collection_name, username, password)

        # Check for data number
        control_collection_nbData(collection, nb_kept_data)

        # Insert kpi json into collection
        collection.insert_one(param_hu.state_kpi)

        # Update connection info
        param_hu.state_perf["mongo"]["connected"] = True
    except:
        param_hu.state_perf["mongo"]["connected"] = False
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
    if(param_hu.state_kpi["ID"] > nb_kept_data):
        to_supress = { "ID": param_hu.state_kpi["ID"] - nb_kept_data }
        collection.delete_one(to_supress)
