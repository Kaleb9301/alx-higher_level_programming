#!/usr/bin/python3
"""
This module contains a class Rectangle with constructor which take
height and widht of the rectangle. to calculat area

"""


class Rectangle:
    """This is an class Rectangle with instance attribute height and width"""
    def __init__(self, width, height):
        """
        initializes height and widt of the rectangle
        upon creation of an instance using property
        getts and setter
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property getter for the widtd"""
        return self.__width

    @width.setter
    def width(self, width):
        """
        Property setter for the width
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("with must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Property getter for the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """
        Property setter fo the height
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
