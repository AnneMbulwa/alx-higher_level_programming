#!/usr/bin/python3
"""subclass square of class rectangle"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """vlass square body
    Args:
        size(int):
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns the area of current square"""
        return (self.__size ** 2)

    def __str__(self):
        """print() should print, and str() should return
        the square description: [Square] <width>/<height>
        """
        return str("[Square] {}/{}".format(self.__size, self.__size))
