#!/usr/bin/python3
"""
This module is of an empty class
"""


class BaseGeometry:
    """An empty class"""

    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if value is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.name = name
        self.value = value

