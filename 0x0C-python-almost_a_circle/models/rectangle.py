#!/usr/bin/python3
"""
class Rectangle that inherits from Base

"""
from models.base import Base

class Rectangle(Base):
    """
    class Rectangle implements Base.
    Methods:
        __init__()
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """init method for Rectangle method
        Args:
            hidth: hidth of rectangle
            height: height of rectangle
            x: an integer
            y: another integer
        Raises:
            TypeError: if the input is not an integer
            ValueError: if an input is negative number
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        Base.__init__(self, id)

    @property
    def height(self):
        """to retreive it"""
        return self.__height

    @height.setter
    def height(self, value):
        """check error and setter for height attribute"""
        if not isinstance(value, int):
                raise TypeError('height must be an integer')
        if value <= 0:
                raise ValueError('height must be > 0')
        self.__height = value

    @property
    def width(self):
        """to retreive it"""
        return self.__width

    @width.setter
    def width(self, value):
        """check error and setter for width attribute"""
        if not isinstance(value, int):
                raise TypeError('width must be an integer')
        if value <= 0:
                raise ValueError('width must be > 0')
        self.__width = value

    @property
    def x(self):
        """to retreive it"""
        return self.__x

    @x.setter
    def x(self, value):
        """chexk error and setter for x attribute"""
        if not isinstance(value, int):
                raise TypeError('x must be an integer')
        if value < 0:
                raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """to retreive it"""
        return self.__y

    @y.setter
    def y(self, value):
        """check error and setter for y attribute"""
        if not isinstance(value, int):
                raise TypeError('y must be an integer')
        if value < 0:
                raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """area of rectangle

        Return:
            area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """display Rectangle with #"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for l in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
                if (j == self.__width - 1):
                    print()

    def __str__(self):
        """return [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                         self.__x, self.__y,
                                                         self.__width,
                                                         self.__height)

    def update(self, *args, **kwargs):
        """
        Updates rectangle class
        Attribute:
            args (list): inputted arguments to updating rectangle class
            kwargs (dict): inputted arguments tu updating rectangle class
        """
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.__width = arg
                if i == 2:
                    self.__height = arg
                if i == 3:
                    self.__x = arg
                if i == 4:
                    self.__y = arg
        elif kwargs is not None and len(kwargs) != 0:
            for (key, value) in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value
