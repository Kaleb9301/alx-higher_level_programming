#!/usr/bin/python3
"""This module conatin Square calss with area fuction which return the area of
the function"""


class Square:
    """This class get size and return area.It has constructor and other addtion
   method called 'area' for this purpose"""
    def __init__(self, size=0):
        """Inializing Square

           Args: size(int)

        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Area of the sqare
            Args: self
            return: int
        """
        return self.__size ** 2
