#!/usr/bin/python3
"""create a square class"""


class Square:
    """class square body"""

    def __init__(self, size):
        """
        Args:
        size(int): size must be int for new square
        """
        self.size = size

    @property
    def size(self):
        """retrives size of current square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns the current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the character #"""
        for a in range(0, self.__size):
            [print("#", end="")for b in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
