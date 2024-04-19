#!/usr/bin/python3
"""This is a module of magic calcultion"""


def magic_calculation(a, b):
    """This fucntion for magic calculation
        Arg: a: int
             b: int
        Return: the differnece between a and b of the magic addtion
    """
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)
    else:
        return (sub(a, b))
