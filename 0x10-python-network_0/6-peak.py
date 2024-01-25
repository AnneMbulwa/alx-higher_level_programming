#!/usr/bin/python3
"""finding a peak in a list of unsorted integers
    algorithm should have the smallest complexity
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list contains integers"""

    if not list_of_integers:
        return None
    list_of_integers.sort()

    return list_of_integers[-1]
