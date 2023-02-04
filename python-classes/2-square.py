#!/usr/bin/python3
""" create a class square """


class Square:
    """ Square class"""

    def __init__(self, size=0):
        """Initialize """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
