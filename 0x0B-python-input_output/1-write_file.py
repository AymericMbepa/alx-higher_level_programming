#!/usr/bin/python3
"""this module writes a string to a text file (UTF8) and
    returns the number of characters written

"""


def write_file(filename="", text=""):
    """write file and return the number of character written"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
