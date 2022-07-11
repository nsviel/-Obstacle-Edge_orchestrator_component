#! /usr/bin/python
#---------------------------------------------


class Hubium:
    # State
    #--------------------
    status = "Offline"
    ip = "127.0.0.1"
    #--------------------

    # Thread
    run_loop = True
    run_thread_con = False
    run_thread_socket = False

    # Socket
    sock_server = None
    sock_server_port = 1

    # HTTP daemon
    http_server_verbose = False
    http_server_port = 1;
    http_server_ip = "";

    # Path
    path_state_hu = "state/state_hu.json"
    path_state_py = "state/state_hu.json"

    path_config = "param/config.json"
    path_geoloc = "data/geo.dat"
    path_image = "data/image/image"
    path_frame = "data/frame/"
    path_predic = "data/prediction/"
    path_generic = "data/generic/"

    def reset(self):
        self.status = "Offline"
