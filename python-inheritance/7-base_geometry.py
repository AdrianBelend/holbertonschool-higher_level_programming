#!/usr/bin/python3
"""empty class"""


class BaseGeometry:
    """empty class"""
    def area(self):
        """Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not str:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be an integer".format(name))
