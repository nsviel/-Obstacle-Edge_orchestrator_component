#! /usr/bin/python
#---------------------------------------------

from src import parameter
from src import mqtt

import json


def get_geo(self):
    print("geo !")

def get_image(self):
    self.send_response(200)
    self.send_header("Content-type", "image/bmp")
    self.end_headers()
    self.wfile.write(load_binary(parameter.path_image))

def get_falsealarm(self):
    mqtt.publish_false_alarm()

def get_test(self):
    self.send_response(200)

def get_is_mqtt_connected(self):
    self.send_response(200)
    self.send_header("Content-type", "application/json")
    self.end_headers()
    file = open('src/state.json')
    jdat = json.dumps(json.load(file))
    self.wfile.write(jdat.encode(encoding='utf_8'))
