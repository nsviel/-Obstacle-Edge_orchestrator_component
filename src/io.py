#! /usr/bin/python
#---------------------------------------------

from src import parameter
from scapy.all import *
from pathlib import Path

import os, os.path
import pcapy


def get_number_file(path):
    if(is_dir_exist(path) == False):
        return 0
    _, _, files = next(os.walk(path))
    return len(files)

def is_dir_exist(path):
    return Path(path).is_dir()

def is_file_exist(path):
    return os.path.isfile(path)

def open_pcap(path):
    pcap = scapy.utils.rdpcap(path)
    return pcap

def get_nb_paquet(pcap):
    nb = 0
    for pkt in pcap:
        if pkt.haslayer(UDP):
            nb += 1
    return nb

def get_size_Gb(path):
    if os.path.exists(path):
        size = os.path.getsize(path) / 1000000000
        return size
    else:
        return 0

def write_data(path, data):
    file = open(path, 'w')
    file.write(data)
    file.close()

def write_pcap(pcap, path, is_append):
    #get file size and convert it into Gb
    if os.path.exists(path):
        size = os.path.getsize(path) / 1000000000
    else:
        size = 0

    #If the file is under 50 Gb save new pcap in file
    if size < 50:
        for pkt in pcap:
            if pkt.haslayer(UDP):
                wrpcap(path, pkt, append=is_append)  #appends packet to output file
            else:
                pass
