#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """intializes the class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("haight", height)
        self.__height = height
