#!/usr/bin/python3
"""returns True if the object is an instance of the class"""


def is_same_class(obj, a_class):
    """returns True if the object is an instance of the specified class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
