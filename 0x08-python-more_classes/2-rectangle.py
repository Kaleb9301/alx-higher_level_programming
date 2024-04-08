#!/usr/bin/python3

"""
This module conatins a class Rectangle which have method for
setting and getting width and heigh and caluclating area and
permeter
"""


class Rectangle:
    """This is ana class Recangle with instacne
        attribute height and width also
        different method for setting and getiing
        height and widht, and calculating area and
        permeter
    """
    def __init__(self, width=0, height=0):
        """
            intializes height and widht of the rectangle:wq
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property getter for the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """property setter fo rthe widht"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >=0")
        self.__width = width

    @property
    def height(self):
        """property getter fo the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Property setter for the height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise TypeError("height must be >= 0")
        self.__height = height

    def area(self):
        """The method area returs the area of therecangl"""
        return self.width * self.height

    def perimeter(self):
        """ Returns the perimeter of the rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
