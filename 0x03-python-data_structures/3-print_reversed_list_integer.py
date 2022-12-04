#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list, in reverse order"""
    if len(my_list) == 0:
        return None
    i = -1
    while i >= -len(my_list):
        print("{:d}".format(my_list[i]))
        i = i - 1
