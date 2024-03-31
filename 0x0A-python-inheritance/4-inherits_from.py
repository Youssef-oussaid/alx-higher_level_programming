#!/usr/bin/python3
"""
this module has the inherits from method
"""


def inherits_from(obj, a_class):
    """checks is an object is of class or a drived/inherited class"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
