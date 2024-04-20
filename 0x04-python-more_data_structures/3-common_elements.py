#!/usr/bin/python3
"""This is the module to find the common element in the two set"""


def common_elements(set_1, set_2):
    """This is a function used to find the common element in two set
        Arg: set_1: set of elements
             set_2: set of elements
        Return: list()
    """
    return (set_1 & set_2)
