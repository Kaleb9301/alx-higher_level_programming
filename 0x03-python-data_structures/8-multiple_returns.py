#!/usr/bin/python3
"""This module return multiple data"""


def multiple_returns(sentence):
    """This functionon that return multiple result
        Arg: sentence: a string that the length and the
             first character is need
        Return: the tuple of int and string from the
                length of the sentence and the first character
    """
    return (len(sentence), sentence[0])
