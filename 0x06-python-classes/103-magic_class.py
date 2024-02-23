#!/usr/bin/python3
"""Define a MagicClass"""


import math

from networkx import radius


class MagicClass:
    """A circle"""
    
    def __init__(self):
        """Initialize a MagicClass
        Args:
            radius (float or int): The radius of a circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be an integer")
        self.__radius = radius
        
    def area(self):
        """Return the area"""
        return (self.__radius ** 2 * math.pi)
    
    def circumference(self):
        """Return the circumference"""
        return (2 * math.pi * self.__radius)
