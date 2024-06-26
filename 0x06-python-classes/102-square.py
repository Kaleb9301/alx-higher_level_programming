#!/usr/bin/python3
"""MY square module"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """Create a Square
        Args: size : lenth of a side of Square
        """
        self.__size = size

    @property
    def size(self):
        """The property of size as the len of a side of Square
            Raises:
                TypeError: if size != int
                ValueError: if size < 0:
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must b an integer')
        if value < 0:
            raise ValueError('size must be >=0')
        self._size = value

    def area(self):
        """Get the area of a Square
        Reeturns: The size squared
        """
        return self.__size ** 2

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()
