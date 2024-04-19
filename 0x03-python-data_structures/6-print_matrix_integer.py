#!/usr/bin/python3
"""This module print matrix"""


def print_matrix_integer(matrix=[[]]):
    """The funciton tha print matrix
        Args: matrix: the matrix to be printed
        Return: None
    """
    for row in matrix:
        for element in row:
            print("{:d}".format(element), end=" ")
        print()
