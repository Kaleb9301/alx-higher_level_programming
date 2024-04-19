#!/usr/bin/python3
"""This module print matrix"""


def print_matrix_integer(matrix=[[]]):
    """The funciton tha print matrix
        Args: matrix: the matrix to be printed
        Return: None
    """
    for row in matrix:
        for i in range(len(row)):
            if i != len(row) - 1:
                print("{:d}".format(row[i]), end=" ")
            else:
                print("{:d}".format(row[i]),)
