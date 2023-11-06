#!/usr/bin/python3
"""function that adds a new attribute to an object if it’s possible:"""


def add_attribute(obj, attr, value):
    """new attribute content
    Args:
        check if new aattribute in dictionary
    Raises
        TypeError
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
