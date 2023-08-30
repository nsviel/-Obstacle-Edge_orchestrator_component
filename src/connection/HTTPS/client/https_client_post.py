#---------------------------------------------
# Possible POST command:
# - /post_command_ai
#       -lidar_height
#       -threshold
# - /post_command_slam
#       -slam_on
#       -slam_off
#       -view_top
#       -view_oblique
#       -reset
# - /post_state_ground
# - /post_state_edge
#---------------------------------------------

from src.connection.HTTPS.client import https_client_fct
import json


def post_command(dest, payload):
    [ip, port, connected] = https_client_fct.network_info(dest)
    command = "/post_command_" + dest
    https_client_fct.send_https_post(ip, port, connected, command, payload)
    terminal.add_post_command(dest, payload)

def post_state(dest, state):
    [ip, port, connected] = https_client_fct.network_info(dest)
    command = "/post_state_" + dest
    payload = json.dumps(state).encode(encoding='utf_8')
    https_client_fct.send_https_post(ip, port, connected, command, payload)
