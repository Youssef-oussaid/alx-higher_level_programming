#!/usr/bin/python3
"""Define a Module"""


class Rectangle:
    """Defines a Class "Rectangle"
    """

    number_of_instances = 0
    """the active instances"""

    print_symbol = '#'
    """type to print"""

    def __init__(self, width=0, height=0):
        """Defines a Rectangle

        Args:
            width (int, optional): the width. Defaults to 0.
            height (int, optional): the height. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for width"""
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

    def area(self):
        """the area"""
        return self.__width * self.__height

    def perimeter(self):
        """the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """the string repr"""
        if not self.__width or not self.__height:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") *
                self.__height)[:-1]

    def __repr__(self):
        """The representation"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """delete an instance
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger of the two rectangles.

        Args:
            rect_1: The First One
            rect_2: The second One
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
