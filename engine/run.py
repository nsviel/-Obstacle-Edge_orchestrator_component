#---------------------------------------------
import subprocess
import os


def start_engine():
    initial_dir = os.getcwd()

    # Get the directory where the executable resides
    executable_dir = os.path.dirname("engine/build/executable")

    # Change the current working directory to the executable directory
    os.chdir(executable_dir)

    # Run the subprocess detached
    subprocess.Popen(["./executable"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    os.chdir(initial_dir)
