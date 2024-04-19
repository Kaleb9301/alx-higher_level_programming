#!/usr/bin/python3
"""This moudle identifies if the element in the list is divisble by 2"""


def divisible_by_2(my_list=[]):
    """The function tha check the number in the list divided by 2
        Arg: my_list: the list of integer
        Return: the boolean result of the check
    """
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return (new_list)
