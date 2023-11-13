#!/usr/bin/python3
import json

"""creating a class base"""

class Base:
    """class base body
    Args:
        __nb_objects(private): private instance
    """
    __nb_objects = 0


def __init__(self, id=None):
    """
    Args:
        id(int): assume id is an intger
    """
    if id is not None:
        self.id = id
    else:
        Base.__nb_objects += 1
        self.id = Base.__nb_objects
