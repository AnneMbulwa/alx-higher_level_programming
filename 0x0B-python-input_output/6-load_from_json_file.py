#!/usr/bin/python3
"""
function that creates an Object from a “JSON file”:
"""
import json


def load_from_json_file(filename):
    """
    Args:
        must use with statement
    """
    with open(filename, 'r', encoding="utf-8") as myfile:
        return json.load(myfile)
