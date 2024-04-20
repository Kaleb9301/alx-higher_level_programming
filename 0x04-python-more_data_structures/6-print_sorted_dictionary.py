#!/usr/bin/python3
"""This module print the sorted dictionary."""


def print_sorted_dictionary(a_dictionary):
    """This function print sorted dictionary
        Args: a_dictionary: dictionary to be sorted and printed
        Return: None
    """
    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
