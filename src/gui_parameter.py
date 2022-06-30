#! /usr/bin/python
#---------------------------------------------

from src import parameter

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


def build_parameter():
    dpg.add_text("Parameter", color=(125, 125, 125))
