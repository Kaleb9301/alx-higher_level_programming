#!/usr/bin/python3
"""This module return the max value in the list"""


def max_integer(my_list=[]):
    """The function that returns the max value for the lisit
        Arg: my_list: the list of integer to be used
        Return: the maximum of the integer in the list
    """
    if len(my_list) == 0:
        return (None)

    big = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > big:
            big = my_list[i]

    return (big)
