#!/usr/bin/python3
"""This moulde if for replacing specific position without modifing
    the orginal list"""


def new_in_list(my_list, idx, new_element):
    """The function that replace element using the copy
        Arg:my_list: the list used for the copy
            idx: the index to be replaced
            new_element: the new element that replace the old
    """
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        new_list = []
        for i in range(0, len(my_list)):
            if i != idx:
                new_list.append(my_list[i])
            else:
                new_list.append(new_element)
        return new_list
