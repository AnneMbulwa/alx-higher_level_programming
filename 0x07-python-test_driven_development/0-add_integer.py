#!/usr/bin/python3
"""function that adds 2 integers.
    a and b must be first casted to integers if they are float
Returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """returns the addition of two integers
    Raises:
        TypeErrors(a or b must be integers
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer") 
    return int(a) + int(b)
