#! /usr/bin/python
#---------------------------------------------

from src import loop
from src import parameter

from gui import callback
from gui import gui_parameter
from gui import gui_runtime
from gui import gui_connection
from gui import gui_loop

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


def start():
    dpg.create_context()

    #Build GUI
    with dpg.window(tag="window", label="Hubium"):
        gui_parameter.build_parameter()
        gui_connection.build_connection()
        gui_runtime.build_runtime()
        build_end()
        #demo.show_demo()

    dpg.create_viewport(title='Hubium', width=parameter.gui_width, height=parameter.gui_height)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("window", True)

    # Init variables
    loop.init()

    # Start main loop program
    while parameter.run and dpg.is_dearpygui_running():
        loop.loop()
        gui_loop.loop()
        dpg.render_dearpygui_frame()

    # Join threads
    loop.exit()

    # Finish program
    dpg.destroy_context()

def build_end():
    dpg.add_separator()
    dpg.add_button(label="close", tag="bclo", callback=callback.callback_event)
