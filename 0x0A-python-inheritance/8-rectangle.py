#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


class BaseGeometry:
    """A class with public instance methods area and integer_validator"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an int and greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A rectangle class that inherits from BaseGeometry"""


    def __init__(self, width, height):
        """intializes the class"""
        self.__width = width
        self.__height = height
        
    def integer_validator(self, width, height):
        """validates the values with base class"""
        return super().integer_validator(width, height)
