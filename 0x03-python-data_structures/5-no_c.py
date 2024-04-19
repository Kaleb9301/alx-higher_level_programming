#!/usr/bin/python3
"""This module remove c f string"""


def no_c(my_string):
    """Remove all character c and C from a string.
        Arg: my_string: the stirng to be used and 'c' and 'C' are remove from
        Return: the string wihtout character 'c' and 'C".
    """
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
