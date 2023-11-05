#!/usr/bin/python3

"""create a class square"""


class Square:
    """class square body"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size(int): new square size
            position(int, int): new position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """retrieves the size of current square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        else value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """retrieves current position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns current area square"""
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
            return

        [print("") for a in range(0, self.__position[1])]
        for a in range(0, self.__size):
            [print(" ", end="") for x in range(0, self.__position[0])]
            [print("#", end="" for z in range(0, self.__size))]
            print("")

     def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for a in range(0, self.__position[1])]
        for a in range(0, self.__size):
            [print(" ", end="") for x in range(0, self.__position[0])]
            [print("#", end="") for z in range(0, self.__size)]
            if a != self.__size - 1:
                print("")
        return ("")
