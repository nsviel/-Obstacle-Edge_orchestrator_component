#! /usr/bin/python
#---------------------------------------------

from param import cla

from src import io


def post_geo():
    io.write_data(cla.hubium.path_geolocalization, post_data.decode('utf-8'))
