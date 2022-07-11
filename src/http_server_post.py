#! /usr/bin/python
#---------------------------------------------

from param import param_hu

from src import io


def post_geo():
    io.write_data(param_hu.path_geolocalization, post_data.decode('utf-8'))
