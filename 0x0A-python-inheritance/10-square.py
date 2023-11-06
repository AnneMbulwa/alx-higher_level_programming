#!/usr/bin/python3
"""defines a subclass square of rectangle"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """class square body
    Args:
        size(int):
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
