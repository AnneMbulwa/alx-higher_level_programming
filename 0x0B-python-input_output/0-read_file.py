#!/usr/bin/python3
"""
function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Args:
        must use the with statement
    """
    with open(filename, encoding="utf-8") as myfile:
        for line in myfile:
            print(line, end="")
