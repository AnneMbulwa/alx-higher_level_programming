#!/usr/bin/python3
"""creating a class Square"""


class Square:
    """class square body"""

    def __init__(self, size=0):
        """
        Args:
            size(int): new square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
