#!/usr/bin/python3
""" Module that contains a function that reads n lines of a text file
"""


def append_write(filename="", text=""):
    """ Function that reads from a file and prints its number of lines
    Args:
        filename: filename
        text: number of lines to print
    Raises
        Exception: when the file can be opened
    """
with open(filename, 'r' encoding="utf-8") as f:
    if text <= 0:
        read_data = f.read()
        print(read_data, end='')
    else:
        num_line = 0
        for line in f:
            print(line, end='')
            num_line +=1
            if num_line == text:
                break
