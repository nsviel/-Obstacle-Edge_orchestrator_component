#! /usr/bin/python
#---------------------------------------------


def write_data(path, data):
    file = open(path, 'w')
    file.write(data)
    file.close()
