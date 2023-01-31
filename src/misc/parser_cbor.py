#---------------------------------------------
import cbor2
import os
import sys


def read_file(path):
    with open(path, 'rb') as f:
        size = os.fstat(f.fileno()).st_size
        while(pos := f.tell()) < size):
            o = cbor2.load(f)
            sys.stdout.write("%08x: time = %d\n" % (pos, o['time']))
            f.read(2)

    sys.stdout.write("Done !")
