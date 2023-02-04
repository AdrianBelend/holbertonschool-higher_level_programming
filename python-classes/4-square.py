#!/usr/bin/python3
""" create a class square """


class Square:
    """ Square class"""

    def __init__(self, size=0):
        """Initialize """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        return self.__size

    def area(self):
        return self.__size ** 2
