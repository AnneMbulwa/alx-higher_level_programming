#!/usr/bin/python3
"""create Square class"""


class Square:
    """class square body"""

    def __init__(self, size=0):
    """
        Args:
        size(int): length of a side of new Square
        """
        self.__size = size

    @property
    def size(self):
        """"
        Raises:
            TypeError: if size != int
            ValueErrorr: if size < 0
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Returns area of cuurent square"""
        return (self.__size * self.__size)

    def __le__(self, other):
        """Defines the <=(less or equal to) comparison"""
        return self.area() <= other.area()

    def __lt__(self, other):
        """Define the <(less) comparison"""
        return self.area() < other.area()

    def __ge__(self, other):
        """Defines the >=(great or equal to) comparison"""
        return self.area() >= other.area()

    def __ne__(self, other):
        """Defines th !=(not equal to) comparison"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Defines the >(great) comparison"""
        return self.area() > other.area()

    def __eq__(self, other):
        """Defines the ==(equal to) comparison"""
        return self.area() == other.area()
