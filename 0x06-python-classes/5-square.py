#!/usr/bin/python3
·''' A class that defines a square by its size '''


class Square:
    def __init__(self, size=0):
        """ Method to initialize the square object
        """
        self.size = size

    def area(self):
        """ Method that returns the square are of the object
        """
        return(self.__size ** 2)

    def my_print(self):
        """ that prints in stdout the square with the character #.
        """
        if self.__size == 0:
            print()
            return()
        for i in range(self.__size):
            print("#" * self.__size)

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
