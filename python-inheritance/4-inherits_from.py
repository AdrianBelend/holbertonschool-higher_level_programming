#!/usr/bin/python3
"""returns True if the object is an instance of the class, otherwise False"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of the specified class"""
    if type(obj) == a_class:
        return False
    else:
        return isinstance(obj, a_class)
