#!/usr/bin/python3
"This module search and replace element in the lsit"


def search_replace(my_list, search, replace):
    """This function replace list element by the data given
        Arg: my_list: this list which element about to replaced
             search: the element to be searche in the list
             replace: the data that used replace the data
        Return: updated list
    """
    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return (new_list)
