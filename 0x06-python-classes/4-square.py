#!/usr/bin/python3
"""Class defines square """


class Square:
    ''' A class that defines a square by its size '''
    def __init__(self, size=0):
        """ Method to initialize the square object.
        """
        self.__size = size

    def area(self):
        """ Method that returns the square are of the object
        """
        return(self.__size ** 2)

    @property
    def size(self):
        """ Method to returns the size value.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Method to set the size value of the square object.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
