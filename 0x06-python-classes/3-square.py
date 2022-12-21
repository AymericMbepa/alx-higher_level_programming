#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author: Aymeric Mbou
"""


class Square:
    """ Define Square

    Attributes:
        size: size of square

    """
    def __init__(self, size=0):
        """ the init methot for Square class

        Args:
            size: the size of square

        Raises:
            TypeError: Exceptin if size is not an integer
            ValueError: Exception if size is less than 0

        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """ function that computr area of square

        Returns:
          the current square area

        """
        return self.__size ** 2
