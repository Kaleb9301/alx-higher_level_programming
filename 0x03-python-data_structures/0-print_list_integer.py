#!/usr/bin/python3

"""This module used for print integer"""


def print_list_integer(my_list=[]):
    """The function that print integer
        Arg: my_list: list of integer to be printed.
        Return: None
    """
    for i in range(len(my_list)):
        print("{}".format(my_list[i]))
