#!/usr/bin/python3

"""this module return the element of the list at some index"""


def element_at(my_list, indx):
    """"This function return the at the indx
        Arg: my_list :the lsit to be used to get the element
             indx: the position that element found
        Return: the element at the index
    """
    if indx < 0:
        return None
    elif indx >= len(my_list):
        return None
    else:
        return my_list[indx]
