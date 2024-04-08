#!/usr/bin/python3

"""
    This modourle constias a call rectangle

"""


class Rectangle:
    """
        This is a calss Recangle with instanc attruboe height and width
        with sevral method

    """
    def __init__(self, width=0, height=0):
        """
        initializes height and width of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property getter for the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """
        property setter for the width
        """
        if type(width) is not int:
            raise TypeError("width must be an intger")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """
        Property getter for the height
        """
        return self._height

    @height.setter
    def height(self, height):
        """
            Property setter for the height
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValurError("height must be >= 0")
        self._height = height

    def area(self):
        """
        The method area() returns the area of the rectangle
        """
        return self.width * self .height

    def perimeter(self):
        """
            Returns the perimeter of the rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
            The Method __str__() is used to return the representation(drawing)
            of the rectang instance uisng  #

            if the width or  height is 0 empyt stiring is rueturned
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
        return "Rectangle({}, {})".format(self.width, self.height)


if __name__ == "__main __":
    import doctest
    doctest.testmod(verbose=True)
