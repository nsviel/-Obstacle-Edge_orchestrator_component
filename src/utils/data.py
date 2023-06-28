#---------------------------------------------
from src.param import param_edge
from src.utils import terminal

import os


def check_directories():
    create_directory(param_edge.path_data_dir)
    create_directory(param_edge.path_image_dir)
    create_or_clear_dir(param_edge.path_frame_dir)
    create_or_clear_dir(param_edge.path_predi_dir)
    set_image_empty()
    terminal.addLog("#", "Data directory checked")

def create_or_clear_dir(path):
    if(os.path.exists(path) == False):
        os.mkdir(path)
        print("[\033[92mOK\033[0m] Directory \033[96m%s\033[0m created" % path)
    else:
        for file in os.scandir(path):
            os.remove(file.path)

def create_directory(path):
    if(os.path.exists(path) == False):
        os.mkdir(path)
        print("[\033[92mOK\033[0m] Directory \033[96m%s\033[0m created" % path)

def set_image_empty():
    command = "cp " + param_edge.path_generic + "image_empty " + param_edge.path_image_dir + "/image"
    os.system(command)
