#!/usr/bin/python3
"""
Write a class MyList that inherits from list:
"""


class MyList(list):
    """Args:
        self(int): assume type is int
    """
    def print_sorted(self):
        c = sorted(self)
        print(c)
