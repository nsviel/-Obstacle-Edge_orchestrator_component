#! /usr/bin/python
#---------------------------------------------

from src import parameter

import dearpygui.dearpygui as dpg


def build_runtime():
    build_data()

def build_data():
    dpg.add_separator()
    dpg.add_text("Data", color=(125, 125, 125))
    with dpg.group(horizontal=True):
        dpg.add_text("Number of frame: [")
        dpg.add_text(0, tag="cpt_nb_frame", color=(31, 140, 250))
        dpg.add_text("]")
    with dpg.group(horizontal=True):
        dpg.add_text("Number of prediction: [")
        dpg.add_text(0, tag="cpt_nb_pred", color=(31, 140, 250))
        dpg.add_text("]")
    with dpg.group(horizontal=True):
        dpg.add_text("Current image: [")
        dpg.add_text("-", tag="cpt_image", color=(31, 140, 250))
        dpg.add_text("]")
    with dpg.group(horizontal=True):
        dpg.add_text("Geolocalization: [")
        dpg.add_text("-", tag="cpt_geo", color=(31, 140, 250))
        dpg.add_text("]")
