#!/usr/bin/python3
"""This module print matrix"""


def print_matrix_integer(matrix=[[]]):
    """The funciton tha print matrix
        Args: matrix: the matrix to be printed
        Return: None
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if j != (len(matrix[i]) - 1):
                print(" ", end="")
        print("")
