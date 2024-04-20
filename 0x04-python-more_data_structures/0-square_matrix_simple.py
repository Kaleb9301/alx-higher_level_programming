#!/usr/bin/python3
"""This module will square the value of the list and store in another list"""


def square_matrix_simple(matrix=[]):
    """This function square the list element store in another list
        Aray: matrix: two dimensional array
        Return: Two dimenesional array
    """
    return ([list(map(lambda x: x * x, row)) for row in matrix])
