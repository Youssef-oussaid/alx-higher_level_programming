#!/usr/bin/python3
"""Define a Module"""


class Rectangle:
    """Define a Class
    """

    def __init__(self, width=0, height=0):
        """Define a Rectangle

        Args:
            width (int): The width. Defaults to 0.
            height (int): The height. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the private instance
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
