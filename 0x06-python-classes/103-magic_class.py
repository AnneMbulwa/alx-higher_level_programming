#!/usr/bin/python3
"""Magic class from ByteCode provide by Holberton"""
import math


class MagicClass:
    """MagicClass body."""

    def __init__(self, radius=0):
        """
        Args:
            radius(float or int): radius for new MgicClass
        """

        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Return of the area of magicclass"""
        return (self._MagicClass__radius ** 2 * math.pi)

    def circumference(self):
        """Calculate the circumference."""
        return (2 * math.pi * self._MagicClass__radius)
