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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the current rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width} / {self.__height}"
