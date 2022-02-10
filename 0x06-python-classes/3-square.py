#!/usr/bin/python3
"""Class define square """


class Square:
    ''' A class that defines a square by its size '''
    def __init__(self, size=0):
        """ Method to initialize the square object.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Method that returns the square are of the object.
        """
        ar = self.__size ** 2
        return (ar)
