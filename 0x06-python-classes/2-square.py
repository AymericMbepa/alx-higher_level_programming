#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@autor: Aymeric Mbepa
"""


class Square:
    """Define Square

    Attributes:
         size: the size of the square
    """


    def __init__(self, size=0):
        """
        the __init__ method for a square class

        Args:
             size: a private instance size

        Raises:
             TypeError: Exception if size is not an integer
             ValueError: Exception if size is less than 0
        """

        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
