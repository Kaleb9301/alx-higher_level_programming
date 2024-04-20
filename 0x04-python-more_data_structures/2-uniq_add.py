#!/usr/bin/python3
"""This mould add and return the sum of unique eleent in this list"""


def uniq_add(my_list=[]):
    """This fucntion add the unique element in the list and return
        the sum
        Arg: my_list: the list used in this function
        Return: the sum of unique element in this set
    """
    sum = 0
    for x in set(my_list):
        sum += x

    return (sum)
