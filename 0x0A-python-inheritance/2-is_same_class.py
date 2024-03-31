#!/usr/bin/python3
"""Module for same class"""


def is_same_class(obj, a_class):
    """checks if object is from a class
    Args:
        obj: the object to check
        a_class: the class to check
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
