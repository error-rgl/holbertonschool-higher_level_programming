#!/usr/bin/python3
"""Class defines square """


class Square:
    ''' A clas that defined a square by its size and position'''
    def __init__(self, size=0, position=(0, 0)):
        """ Method to inicialize the square object.
        """
        self.__size = size
        self.__position = position

    def area(self):
        """ Method that returns the square are of the object
        """
        return(self.__size ** 2)

    def my_print(self):
        """ Method that prints in stdout the square with the character #.
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print(" " * self.__position[0], end="")
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

    @property
    def position(self):
        """ Method to returns the position value.
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Method to set the position value of the square object.
        """
        if type(value) is not tuple\
            and type(value[0]) is not int\
                and type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
