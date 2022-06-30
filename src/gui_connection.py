#! /usr/bin/python
#---------------------------------------------

from src import parameter

import dearpygui.dearpygui as dpg


def build_connection():
    dpg.add_separator()
    dpg.add_text("Connection", color=(125, 125, 125))
    with dpg.group(horizontal=True):
        dpg.add_text("HTTP server: [")
        dpg.add_text("OFF", tag="qhttpserv", color=(31, 140, 250))
        dpg.add_text("]")
    with dpg.group(horizontal=True):
        dpg.add_text("MQTT SNCF: [")
        dpg.add_text("OFF", tag="smqttsncf", color=(31, 140, 250))
        dpg.add_text("]")
    with dpg.group(horizontal=True):
        dpg.add_text("Socket Pywardium: [")
        dpg.add_text("OFF", tag="ssocketpy", color=(31, 140, 250))
        dpg.add_text("]")
    with dpg.group(horizontal=True):
        dpg.add_text("Socket Velodium: [")
        dpg.add_text("OFF", tag="ssocketve", color=(31, 140, 250))
        dpg.add_text("]")
    with dpg.group(horizontal=True):
        dpg.add_text("Socket Edge: [")
        dpg.add_text("OFF", tag="ssocketed", color=(31, 140, 250))
        dpg.add_text("]")
