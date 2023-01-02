#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """a class Rectangle that defines a rectangle by


    Attributes:
           width: width of rectangle
           height: height of rectangle
    """
    def __init__(self, width=0, height=0):
        """init methof for rectangle class

        Args:
           width: width of rectangle
           height: heightt of  rectangle
        """
        self.__width = width
        self.__height = height
    @property
    def width(self):
        """ to retreive width of rectangle

        Return:
             width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ check error and setter for width attribute

        Args:
           value: value to checking error
        Raises:
           TypeError:exception if type is not an integer
           ValueError: exception if width is less than 0
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__height
    @height.setter
    def height(self, value):
        """ check for error and setter for height attribute

        Args:
           value: value to checking error
        Raises:
           TypeError:exception if type is not an integer
           ValueError: exception if width is less than 0
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
