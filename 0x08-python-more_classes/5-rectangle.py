#!/usr/bin/python3

"""
This module contains a class Rectangle
"""


class Rectangle:
    """This is an clas Rectangle with instance attribute height and width"""
    def __init__(self, width=0, height=0):
        """
        initializes heiht and width of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property getter for the wideth"""
        return self.__width

    @width.setter
    def width(self, width):
        """
        property setter for the width
        """
        if type(width) is not int:
            raise TypeErro("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Property gett for theheight"""
        return self.__height

    @height.setter
    def height(self, height):
        """
        property setter for the height

        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise TypeError("height must be >= 0")
        self.__height = height

    def area(self):
        """
        This method area() returns area of the rectangle
        bby take the prodict of the width and hiehgt of the
        rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        The method perimeter() return the perimeter of the
        rectangel by taking the sum of width and height of the
        rectangle, then muliplying the result by 2
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        The method __str() is used to return the representation (draing) of
        rectangle instance using

        """
        if self.width == 0 or self.height == 0:
            return ""
        shape_rep_array = []
        for height in range(self.height):
            shape_rep_array.append("#" * self.width)
            shape_rep_array.append("\n")
        shape_rep_array.pop()
        return "".join(shape_rep_array)

    def __repr__(self):
        return "Rectangle({}, {}".fomate(self.width, self.height)

    def __del__(self):
        print("Bye reectangle...")


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
