#!/usr/bin/python3
"This module try to print a square size hashes(#)"


class Square:
    """This class contain addition myprint method other than others"""
    def __init__(self, size):
        """Intitiazing the object
            Args:
                self:
                size(int): the size of the side of the square
        """
        self.__size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
