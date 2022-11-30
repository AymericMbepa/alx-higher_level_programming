#!/usr/bin/python3
def islower(c):
    """ checks for lowercase character."""
    if ord(c) >= 97 and ord(c) <= 122:
        result = True
    else:
        result = False
    return result
