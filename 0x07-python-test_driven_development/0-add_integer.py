#!/usr/bin/python3
"""function that adds 2 integers.
    a and b must be first casted to integers if they are float
Returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    if not instance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not instance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
if __name__ == "__main__":
    doctest.testfile("tests/0-add_integer.txt")
