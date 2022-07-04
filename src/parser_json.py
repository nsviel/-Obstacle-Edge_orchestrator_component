#! /usr/bin/python
#---------------------------------------------

from src import parameter

import json


def get_json_encoded():
    file = open(parameter.path_state)
    data = json.load(file)
    data_encoded = json.dumps(data).encode(encoding='utf_8')
    return data_encoded

def update_state_json(lvl1, lvl2, state):
    file = open(parameter.path_state, "r")
    data = json.load(file)
    if(data[lvl1][lvl2] !=state):
        data[lvl1][lvl2] = state
        file = open('src/state.json', "w")
        json.dump(data, file, indent=4)
        file.truncate()
