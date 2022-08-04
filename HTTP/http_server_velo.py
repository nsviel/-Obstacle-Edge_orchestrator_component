#! /usr/bin/python
#---------------------------------------------

from HTTP import http_client_get


def process_post_data(option, value):
    if(option == "slam"):
        if(value == "True"):
            http_client_get.get_command_ve("\slam_on")
        if(value == "False"):
            http_client_get.get_command_ve("\slam_off")
    elif(option == "view"):
        if(value == "Top"):
            http_client_get.get_command_ve("\view_top")
        if(value == "Oblique"):
            http_client_get.get_command_ve("\view_oblique")
