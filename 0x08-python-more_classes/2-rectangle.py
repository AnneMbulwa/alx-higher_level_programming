#!/usr/bin/python3
"""creating a class rectangle"""


class Rectangle:
    """class body"""

    def __init__(self, width=0, height=0):
        """
        Args:
            width(int): new width
            height(int): new height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves current width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the current height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the current area of rectagle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
