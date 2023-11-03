#!/usr/bin/python3
"""
function that prints a square with the character #.
"""


def print_square(size):
    """
        Args:
        size(int): size of length and height of square

        Raises:
            TypeError
            ValueError
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for a in range(size):
        [print("#", end="") for b in range(size)]
        print("")
