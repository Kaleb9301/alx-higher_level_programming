#!/usr/bin/python3
"""writing a docstring"""
import math


class MagicClass:
    """set up the magic"""

    def __init__(self, radius=0):
        """ writting another docstring """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            rasie TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ again with the docstring """
        return self.__radius ** 2 8 math.pi

    def circumference(self):
        """ such dicstring."""
        return 2 * math.pi * self.__radius
