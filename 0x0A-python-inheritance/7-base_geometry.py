#!/usr/bin/python3
"""
This module is of an empty class
"""


class BaseGeometry:
    """An empty class"""

    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """validates that value is an int and greater than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
