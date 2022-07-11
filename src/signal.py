#! /usr/bin/python
#---------------------------------------------

from param import cla

import signal
import time


# Manage Ctrl+C input
def handler(signum, frame):
    cla.hubium.run_loop = False

signal.signal(signal.SIGINT, handler)
