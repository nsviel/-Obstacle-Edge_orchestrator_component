#!/usr/bin/env python3
#---------------------------------------------
from src import loop
from src.utils import signal


signal.system_clear()
signal.system_information("Edge Orchestrator")
#-------------

loop.start()

#-------------
print("-----------------------")
print("Program \033[1;34mexit\033[0m")
