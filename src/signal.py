#! /usr/bin/python
#---------------------------------------------

from param import classes

import signal
import time


# Manage Ctrl+C input
def handler(signum, frame):
    classes.hubium.run_loop = False

signal.signal(signal.SIGINT, handler)
