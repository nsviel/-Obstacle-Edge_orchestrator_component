#---------------------------------------------

# State
state_edge = {}
state_ground = {}
state_network = {}
state_control = {}
state_cloud = {}

# Thread
run_loop = True
run_thread_con = False
run_thread_socket = False
run_thread_perf = False

# Socket
sock_client = None
sock_client_ok = False

# HTTP
https_server = None
http_server_daemon = None
http_server_ip = "";

# MQTT
mqtt_client  = None
mqtt_msg = 'hello world'

# Tic delay
tic_loop = 1
tic_message = 0.05
tic_connection = 0.5
tic_network = 0.5

# State file
path_state_current = "src/state/current/"
path_state_initial = "src/state/initial/"

# Data dir
path_data_dir =  "../data"
path_image_dir = "../data/image"
path_frame_dir = "../data/frames"
path_predi_dir = "../data/prediction"
path_generic = "src/param/generic/"

# Data file
path_geoloc = "../data/geo.dat"
path_image = "../data/image/image"
