#!/usr/bin/python3
"""returns True if the object is an instance of the class, otherwise False"""


def is_same_class(obj, a_class):
    """returns True if the object is an instance of the specified class""" 
    if type(obj) == a_class:
        return True
    else:
        return False
