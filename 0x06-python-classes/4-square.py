#!/usr/bin/python3
"""In this module we include methodw in Square calls inored to get the
print out the size"""


class Square:
    """This class for squre"""
    def __init__(self, size=0):
        """Initializing square

           Args: size(int)
        """
        self.__size = size

    @property
    def size(self):
        """size getter
            Args:
                self
            return:
                size of the side(int)
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Size setter
            Args:
                self:
                value(int): the size to be set.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value:
            self.__size = value

    def area(self):
        """Return the current area of the square. """
        return (self.__size ** 2)
