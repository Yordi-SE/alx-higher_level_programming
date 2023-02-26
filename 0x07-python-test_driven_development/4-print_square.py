#!/usr/bin/python3
"""This Module contains the defination of the
    Function that we used to square with the
    character #
    """


def print_square(size):
    """Here we put the defination of
        the function
        """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if not isinstance(size, int) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
