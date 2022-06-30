#! /usr/bin/python
#---------------------------------------------

from src import parameter

import dearpygui.dearpygui as dpg


def callback_event():
    parameter.run = dpg.get_value("bclo")
