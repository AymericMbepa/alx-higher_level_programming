#!/usr/bin/python3
def uppercase(str):
    """prints a string in uppercase followed by a new line"""
    for i in str:
        if ord(i) > 96:
            i = chr(ord(i) - 32)
        print('{}'.format(i), end='')
