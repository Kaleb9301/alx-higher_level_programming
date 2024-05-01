#!/usr/bin/python3
"""This module print the reversed order of the list"""


def print_reversed_list_integer(my_list=[]):
    """The function that print the revers order of the list
        Arg: my_list: the list to be printed
        Return: None
    """
    if my_list:
        for i in reversed(my_list):
            print("{:d}".format(i))
