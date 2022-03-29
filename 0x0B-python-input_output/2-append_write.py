#!/usr/bin/python3
""" Module that contains a function that reads n lines of a text file
"""


def append_write(filename="", text=""):
    """ Function that reads from a file and prints its number of lines
    Args:
        filename(str): filename
        text(str): string to append
    """
    with open(filename, "a", encoding="UTF-8") as file:
        return file.write(text)
