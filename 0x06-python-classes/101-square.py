#!/usr/bin/python3
"""my square module"""


class Square:
    """define a Square."""

    def __str__(self):
        """teach python to print the square my way"""
        return self.pos_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """ initialize the square with this
        Args:
            size: a side of square
            postion: whare the square is (coordinates)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """property of the length of a side of square
            Raises:
            TypeError: is size is not an int
            ValuError: is size is < 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ set the size of square
        Args:
            value: the size
        Raises:
            TypeError: if value is not int
            ValueError: is value < 0
        """
        if not isinstance(value, int):
            raise TypeError('size must be an intger')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def postion(self):
        """property of the postion of square
        Raises:
            TypeError: if value != tuple of 2 ints >= 0.
        Returns: the postion
        """
        return self.__position

    @postion.setter
    def position(self, value):
        """ set the postion
        Args:
            value: where
        Raises:
            TypeError: if not tuple, ints, postive
        Returns: the position
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 postive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """ the area of square
        Returns:
        size * size
        """
        return self.__size ** 2

    def pos_print(self):
        """returns the printed square with postion"""
        pos = ""
        if not self.size:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.postion[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """print square."""
        print(self.pos_print(), end="")
