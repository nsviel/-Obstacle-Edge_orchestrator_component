#! /usr/bin/python
#---------------------------------------------

from param import param_hu

import os


def check_directories():
    create_directory(param_hu.path_data_dir)
    create_or_clear_dir(param_hu.path_image_dir)
    create_or_clear_dir(param_hu.path_frame_dir)
    create_or_clear_dir(param_hu.path_predi_dir)

def create_or_clear_dir(path):
    if(os.path.exists(path) == False):
        os.mkdir(path)
        print("[\033[92mSSD\033[0m] Directory %s created" % path)
    else:
        for file in os.scandir(path):
            os.remove(file.path)

def create_directory(path):
    if(os.path.exists(path) == False):
        os.mkdir(path)
        print("[\033[92mSSD\033[0m] Directory %s created" % path)
