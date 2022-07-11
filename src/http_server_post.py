#! /usr/bin/python
#---------------------------------------------

from param import classes

from src import io


def post_geo():
    io.write_data(classes.hubium.path_geolocalization, post_data.decode('utf-8'))
