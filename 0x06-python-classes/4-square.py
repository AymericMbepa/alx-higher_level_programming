#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Aymeric Mbepa

"""


class Square:
    """ Define Square

    Attributes:
            size: size of square

    """
    def __init__(self, size=0):
        """ __init__ methot for Square class

        Args:
            size: size of square

        """
        self.__size = size

    @property
    def size(self):
        """call the function to checking property

        Return:
            the size of the square

        """
        return self.__size


    @size.setter
    def size(self, value):
        """check error and setter for size attribute

        Args:
            value: value to checking error

        Raises:
            TypeError: Exceptin if size in not an integer
            ValueError: Exception if size is less than 0

        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """ compute area of square

        Returns:
             the area of square

        """
        return self.__size ** 2
