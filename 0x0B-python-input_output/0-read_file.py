#!/usr/bin/python3
"""
this module read a text file
@AUTHOR: Aymeric Mbepa

"""


def read_file(filename=""):
    """
    read text file
    Arguments:
        filename: the name of the file to open
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end ='')
