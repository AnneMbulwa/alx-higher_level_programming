#!/usr/bin/python3
"""
function that prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Args:
        text(str): text must be string
    Raises:
        TypeError
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = ".?:"
    a = 0

    while a < len(text) and text[a] == " ":
        a += 1

    while a < len(text):
        print(text[a], end="")
        if text[a] == "\n" or text[a] in characters:
            if text[a] in characters:
                print("\n")
            a += 1
            while a < len(text) and text[a] == " ":
                a += 1
            continue
        a += 1
