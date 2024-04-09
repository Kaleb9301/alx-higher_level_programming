#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
The 2-matix_divided module supplies one function, matrix _divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """Divides all elements in the matrix by div"""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for list_kind in matrix:
        if type(list_kind) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(list_kind)
        elif size != len(list_kind):
            raise TypeError("Each row of the matrix must have the same size")
        for i in list_kind:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in list_kind] for list_kind in matrix]
