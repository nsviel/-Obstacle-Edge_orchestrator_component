#---------------------------------------------

# State
state_hu = {}
state_py = {}
state_perf = {}
state_kpi = {}
state_pred = {}

# Thread
run_loop = True
run_thread_con = False
run_thread_socket = False
run_thread_perf_client = False
run_thread_perf_server = False

# Socket
sock_server_l1 = None
sock_server_l2 = None
sock_client = None
sock_client_ok = False

# HTTP
https_server = None
http_server_daemon = None
http_server_ip = "";

# MQTT
mqtt_client  = None
mqtt_msg = 'hello world'

# Perf
process_client_iperf = None
process_server_iperf = None

# State
path_config = "param/config.json"
path_state_hu = "state/state_hu.json"
path_state_py = "state/state_py.json"
path_state_perf = "state/state_perf.json"
path_state_kpi = "state/state_kpi.json"
path_state_pred = "state/state_pred.json"

# Data
path_data_dir = "data"
path_image_dir = "data/image"
path_frame_dir = "data/frame/"
path_predi_dir = "data/prediction/"

path_geoloc = "data/geo.dat"
path_image = "data/image/image"
path_generic = "data/generic/"

def info_connection(ip, port, connected):
    print(" ")
    print("--------------")
    print(ip)
    print(port)
    print(connected)
