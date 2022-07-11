#! /usr/bin/python
#---------------------------------------------


class Lidar:
    # LiDAR 1
    l1_speed = 600
    l1_device = "enxf8e43b6cecab"
    l1_ip = "http://192.168.1.201/cgi/setting"
    l1_nb_packet = 0

    # LiDAR 2
    l2_speed = 600
    l2_device = "enxf8e43b6cdf6c"
    l2_ip = "http://192.168.1.202/cgi/setting"
    l2_nb_packet = 0

    # State
    l1_connected = False
    l2_connected = False
    time_capture = 0

    # Path
    path_capture = ""
    path_dir_l1 = ""
    path_dir_l2 = ""
    path_file_l1 = ""
    path_file_l2 = ""
    path_add = ""
    file_name = ""

    def reset(self):
        self.l1_nb_packet = 0
        self.l2_nb_packet = 0
        self.l1_connected = False
        self.l2_connected = False
        self.time_capture = 0
