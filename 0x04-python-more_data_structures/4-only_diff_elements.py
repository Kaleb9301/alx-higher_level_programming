#!/usr/bin/python3
"""This is the moule to returns a set of allelemts present in only one set"""


def only_diff_elements(set_1, set_2):
    """This funcition returns the set of all elemnt
       only one set
       Arg: set_1: set of element
            set_2: set of element
       Return: return the list of elemetn present in only one set
    """
    return (set_1 ^ set_2)
