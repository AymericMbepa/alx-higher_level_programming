#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """this represents a rectangle"""

    def __init__(self, width=0, height=0):
        """init methof for rectangle class

        Args:
           width: width of rectangle
           height: heightt of  rectangle

        Raises:
           TypeError: if size is not integer
           ValueError: if size is less than zero
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ to retreive width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ check error and setter for width attribute
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
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """area of rectangle

        Return:
           area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """rectangle perimeter

        Return:
           rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """presents a diagram of the rectangle defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += "#"
            if i < self.__height - 1:
                rectangle += '\n'
        return rectangle

    def __repr__(self):
        """return a string representation of the rectangle to be able to
        recreate a new instance """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print the message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
