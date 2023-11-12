#!/usr/bin/python3
"""
function that inserts a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Args:
        must contain with statement
        don’t need to manage file permission / file doesn't exist exceptions
    """
    with open(filename, 'r') as myfile:
        a = myfile.readlines()

    with open(filename, 'w') as myfile1:
        x = ""
        for line in a:
            x += line
            if search_string in line:
                x += new_string
        myfile1.write(x)
