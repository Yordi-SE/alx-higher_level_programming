#!/usr/bin/python3
"""This Module contains The defination of
    function we use to print full name of
    a person"""


def say_my_name(first_name, last_name=""):
    """Here we define the body of
    the function"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
