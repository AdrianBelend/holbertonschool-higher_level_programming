#!/usr/bin/python3
"""empty class"""


class BaseGeometry:
    """empty class"""

    def area(self):
        """Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validation"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be na integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
