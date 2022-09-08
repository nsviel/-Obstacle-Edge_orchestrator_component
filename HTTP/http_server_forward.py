#! /usr/bin/python
#---------------------------------------------

from HTTP import http_client_get


def forward_ve_post_data(option, value):
    if(option == "slam"):
        if(str(value) == "True"):
            http_client_get.get_command_ve("/slam_on")
        if(str(value) == "False"):
            http_client_get.get_command_ve("/slam_off")
    elif(option == "view"):
        if(value == "Top"):
            http_client_get.get_command_ve("/view_top")
        if(value == "Oblique"):
            http_client_get.get_command_ve("/view_oblique")
