#!/usr/bin/python
"""This module it to dived one list elemt by other"
"""


def list_division(my_list_1, my_list_2, list_length):
    """Function to divide list
        Args: my_list_1: the first list or dividend list
              my_list_2: the second list or divisor list
              list_length: the number of element in the list
        Returns:
                new_lists: have element of quitiont of the above list operation
    """
    new_list = []
    result = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)

    return (new_list)
