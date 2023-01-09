#!/usr/bin/python3
"""
this module prints the list, but sorted (ascending sort)

"""


class MyList(list):
    """prints the list, but sorted (ascending sort)

    """
    def print_sorted(self):
        """ print sorted list"""
        print(sorted(self))
