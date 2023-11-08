#!/usr/bin/python3
"""function that returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """
    Args:
        my_obj(obj):
    Return
        json format of the object
    """
    return json.dumps(my_obj)
