#!/usr/bin/python3
"""create a class basegeometry"""


class BaseGeometry:
    """class basegeometry body"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Args:
            name(str):
            value(int):
        Raises.
            TypeError and ValueError
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
