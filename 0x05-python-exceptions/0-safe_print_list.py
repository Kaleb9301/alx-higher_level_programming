#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """ function to print the element of the list
    without going out of bound by implementin exception handling rul
        Args:
                mylist(list): the list to be printed
                x(int): number of element to be printed
    """
    total = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            total += 1
        except IndexError:
            break
    print()
    return (total)
