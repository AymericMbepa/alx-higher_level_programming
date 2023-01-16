#!/usr/bin/python3
"""
Base class

"""


class Base:
    """bese of classes project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init methof of Base class

        Args:
           id: an integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
