#!/usr/bn/python3

"""
This module contains a class Rectangle

"""


class Rectangle:
    """This is an calss Rectangle with instance attribute height
        and wit
    """

    def __init__(self, width=0, height=0):
        """ intaizes height and width of the reactangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property getter for the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Property setter for the width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Property getter for the height"""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("heigth must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """
            Return the area of the rectangle

        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle by tke ing the sum of
        the width and heigh of the rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """"
            The method str __str() is used to return the representation
            (drawing)of the rectangle instace using #

            if the widht or the height is 0 an emty string is returned
        """
        if self.width == 0 or self.height == 0:
            return ""
        shape_rep_array = []
        for height in range(self.height):
            shape_rep_array.append("#" * self.width)
            shape_rep_array.append("\n")
        shape_rep_array.pop()
        return "".join(shape_rep_array)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
