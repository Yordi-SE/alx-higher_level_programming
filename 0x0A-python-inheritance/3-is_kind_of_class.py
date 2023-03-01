#!/usr/bin/python3
"""This module contain the defination
    of function that check if a object
    is instance of a class
    """


def is_kind_of_class(obj, a_class):
    """Here we define the
    function
    """
    if isinstance(obj, a_class):
        return True
    return False
