#! /usr/bin/python
#---------------------------------------------


class Pywardium:
    # State
    #--------------------
    status = "Offline"
    ip = "127.0.0.1"
    #--------------------

    # Connection
    http_connected = False
    socket_connected = False

    # Socket
    http_server_port = 1
    sock_server_port = 1
    sock_client = None

    # Geolocalization
    geo_country = "France"

    def reset(self):
            self.status = "Offline"
            self.http_connected = False
            self.socket_connected = False
            self.geo_country = "France"
