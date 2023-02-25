#!/usr/bin/python3

"""addition function
    This Module contains the defination of
    function that used to add integers
"""


def add_integer(a, b=98):
    """Here we define function that return sum of its arguments
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    """Here we cast floats to integers if any
    """
    x, y = (int(i) for i in [a, b])
    return x + y
