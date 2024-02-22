#!/usr/bin/python3
"""Square Module."""


class Square:
    """Define a square."""

    def __init__(self, size=0):
        """constructor

        Args
            size: Length of a side of a square

        Raises:
            TypeError: if size is not an int
            ValueError: if less than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
