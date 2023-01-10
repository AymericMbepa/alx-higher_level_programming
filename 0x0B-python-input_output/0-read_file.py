#!/usr/bin/python3
"""
this module read a text file

"""


def read_file(filename=""):
    """read text file"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end ='')
