#!/usr/bin/python3
""" Module that contains a function that reads n lines of a text file
"""


def append_write(filename="", text=""):
    """ Function that reads from a file and prints its number of lines
    Args:
        filename: filename
        text: append write
    Raises
        Exception: when the file can be opened
    """
with open(filename, 'a' encoding="utf-8") as f:
    return(f.write(text))
