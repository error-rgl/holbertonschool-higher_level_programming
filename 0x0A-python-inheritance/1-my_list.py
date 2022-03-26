#!/usr/bin/python3
"""Class definition"""


class MyList(list):
    """Class MyList inherited"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
