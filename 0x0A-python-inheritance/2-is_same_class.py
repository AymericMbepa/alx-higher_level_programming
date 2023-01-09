#!/usr/bin/python3
"""
this module returns True if the object is exactly an
instance of the specified class ; otherwise False

"""


def is_same_class(obj, a_class):
    """return true if the object is an instance of class specified"""
    return type(obj) == a_class
