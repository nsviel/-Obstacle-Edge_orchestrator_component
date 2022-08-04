#! /usr/bin/python
#---------------------------------------------

from param import param_hu

from HTTP import http_server_fct
from HTTP import http_client_get
from SOCK import sock_server
from MQTT import mqtt_publish

from src import parser_json
from src import io

import json


def get_geo(self):
    print("geo !")

def get_image(self):
    http_server_fct.send_image(self, param_hu.path_image)

def get_false_alarm(self):
    mqtt_publish.publish_false_alarm()

def get_restart_sock_server():
    sock_server.restart_daemon()

def get_lidar_1_start():
    http_client_get.get_command_py("/lidar_1_start", "[#] Lidar 1 start")

def get_lidar_1_stop():
    http_client_get.get_command_py("/lidar_1_stop", "[#] Lidar 1 stop")

def get_lidar_2_start():
    http_client_get.get_command_py("/lidar_2_start", "[#] Lidar 2 start")

def get_lidar_2_stop():
    http_client_get.get_command_py("/lidar_2_stop", "[#] Lidar 2 stop")

def get_test_http_conn(self):
    self.send_response(200)

def get_state_hu(self):
    http_server_fct.send_state(self, param_hu.path_state_hu)

def get_state_py(self):
    http_server_fct.send_state(self, param_hu.path_state_py)
