#!/usr/bin/python3
"""define a class rectangle that inherits the methods from basegeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """class rectangle that inherits from basegeometry
    Args:
        width(int):
        height(int):
    integer_validator to ensure both width and height are integers
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
