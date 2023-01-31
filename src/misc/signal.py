#---------------------------------------------
from src.misc import connection
from src.param import param_hu

import socket
import platform
import signal
import time
import os
import sys


# Manage Ctrl+C input
def handler(signum, frame):
    param_hu.run_loop = False

signal.signal(signal.SIGINT, handler)

def system_clear():
    os.system('clear')

def check_for_root():
    if not os.geteuid() == 0:
        sys.exit("\nOnly root can run this script\n")

def system_information(prog_name):
    check_for_root()

    #Info
    program = prog_name
    ip = connection.get_ip_adress()
    hostname = socket.gethostname()
    arch = platform.architecture()[0]
    core = platform.uname()[2]
    proc = platform.processor()
    python = platform.python_version()

    try:
        OS = platform.freedesktop_os_release()['PRETTY_NAME']
    except:
        OS = platform.system()

    #Header
    print("    : : \033[1;34m%s\033[0m : :    "% program)
    print("-----------------------")
    print('%-10s' '\033[1;34m%s\033[0m' % ("IP", ip))
    print('%-10s' '\033[1;34m%s\033[0m' % ("Hostname", hostname))
    print('%-10s' '\033[1;34m%s\033[0m, \033[1;34m%s\033[0m' % ("Arch", arch, proc))
    print('%-10s' '\033[1;34m%s\033[0m' % ("OS", OS))
    print('%-10s' '\033[1;34m%s\033[0m' % ("Core", core))
    print('%-10s' '\033[1;34m%s\033[0m' % ("Python", python))
    print("-----------------------")

class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    def __exit__(self, type, value, traceback):
        signal.alarm(0)
