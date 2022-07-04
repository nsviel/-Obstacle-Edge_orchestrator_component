#! /usr/bin/python
#---------------------------------------------

from src import parameter

import signal
import time


# Manage Ctrl+C input
def handler(signum, frame):
    parameter.run_loop = False

signal.signal(signal.SIGINT, handler)
