#!/usr/bin/python3
"""This module contains the defination of
    The function that checks of the object
    is inherited from a class
    """


def inherits_from(obj, a_class):
    """here we put the body
    of the function
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
