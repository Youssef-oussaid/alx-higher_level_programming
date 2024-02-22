#!/usr/bin/python3
"""Square Module."""


class Square:
    """Define a square."""

    def __init__(self, size=0):
        """constructor

        Args
            size: Length of a side of a square
        """
        self.size = size

    @property
    def size(self):
        """property for the length of a side of a square
        
        Raises:
            TypeError: if size is not an int
            ValueError: if less than 0
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
    
    def area(self):
        """Area of this square
        Returns:
            the size of the square
        """
        return self.__size ** 2
