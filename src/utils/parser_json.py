#---------------------------------------------
from src.param import param_edge

import json
import os


def load_state(path):
    try:
        file = open(path, "r")
        data = json.load(file)
        return data
    except:
        print("[error] Problem loading state at %s"% path)

def load_state_utf8(path):
    try:
        file = open(path, "r")
        data = json.load(file)
        data_encoded = json.dumps(data).encode(encoding='utf_8')
        return data_encoded
    except:
        print("[error] Problem loading utf8 state at %s"% path)

def load_data_from_file(path):
    file = open(path, "r")
    data = json.load(file)
    return data

def load_data_from_file_b(path):
    f = open(path)
    data = json.dumps(json.load(f))
    return data

def upload_file(path, data):
    file = open(path, "w")
    json.dump(data, file, indent=4)

def update_state_file(path, data):
    if(len(data) != 0):
        file = open(path, 'w')
        data_loaded = json.loads(data)
        json.dump(data_loaded, file, indent=4)
