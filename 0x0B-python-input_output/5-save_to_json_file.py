#!/usr/bin/python3
"""
function that writes an Object to a text file, using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Args:
        must use with statement
    """
    with open(filename, 'w') as myfile:
        json.dump(my_obj, myfile)
