#!/usr/bin/python3
"""This module print the reversed order of the list"""


def print_reversed_list_integer(my_list=[]):
    """The function that print the revers order of the list
        Arg: my_list: the list to be printed
        Return: None
    """
    for i in range(len(my_list) - 1, 0, -1):
        print("{:d}".format(my_list[i]))
