#! /usr/bin/python
#---------------------------------------------


# State
state_hu = {}
state_py = {}

# Thread
run_loop = True
run_thread_con = False
run_thread_socket = False

# Socket
sock_server = None

# HTTP
http_server = None
http_server_daemon = None
http_server_verbose = False
http_server_ip = "";

# MQTT
mqtt_client  = None
mqtt_msg = 'hello world'

# State
path_config = "param/config.json"
path_state_hu = "state/state_hu.json"
path_state_py = "state/state_py.json"

# Data
path_geoloc = "data/geo.dat"
path_image = "data/image/image"
path_frame = "data/frame/"
path_predi = "data/prediction/"
path_generic = "data/generic/"
