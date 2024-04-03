#!/usr/bin/python3i
"""This module do print integer and handle
    exception
"""


def safe_print_integer(value):
    """ The function that print the value if the
        the value is integer and handle exception
        Args:
                value(int): the number to printed
    """

    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
