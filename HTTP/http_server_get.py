#! /usr/bin/python
#---------------------------------------------

from param import param_hu

from HTTP import http_server_fct
from MQTT import mqtt_publish

from src import parser_json
from src import io

import json


def get_geo(self):
    print("geo !")

def get_image(self):
    http_server_fct.send_image(self, param_hu.path_image)

def get_falsealarm(self):
    mqtt_publish.publish_false_alarm()

def get_test_http_conn(self):
    self.send_response(200)

def get_state_hu(self):
    http_server_fct.send_state(self, param_hu.path_state_hu)

def get_state_py(self):
    http_server_fct.send_state(self, param_hu.path_state_py)
