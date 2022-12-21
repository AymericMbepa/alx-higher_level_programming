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
    def __init__(self, size=0, position=(0, 0)):
        """ __init__ methot for Square class

        Args:
            size: size of square
            position: tuple of 2 positive integers

        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """call the function to checking property

        Returns:
            the size of the square

        """
        return self.__size

    @property
    def position(self):
        """call the function to checking property

        Returns:
            a tuple of positions

        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """chexk error and setter for position attribute

        Args:
            value: value to checking error

        Raises:
            TypeError: Exception if positions elements does not integers

        """
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[1]) is not int or type(value[0]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """ compute area of square

        Returns:
             the area of square

        """
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the character #

        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            if self.__position[0] > 0:
                for k in range(self.__position[0]):
                    print('-', end='')
            for j in range(self.__size):
                print('#', end='')
            print()
