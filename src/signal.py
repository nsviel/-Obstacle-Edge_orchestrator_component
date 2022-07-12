#! /usr/bin/python
#---------------------------------------------

from param import param_hu

import signal
import time


# Manage Ctrl+C input
def handler(signum, frame):
    param_hu.run_loop = False

signal.signal(signal.SIGINT, handler)
