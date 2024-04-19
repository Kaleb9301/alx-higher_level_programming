#!/usr/bin/python3

"""This module replace element in the list"""


def replace_in_list(my_list, idx, element):
    """This function replace element in the list
        Arg: my_list: the list to be used
             indx: the position to be replaced
             element: the replacing data\
        return: The updated list
    """
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
