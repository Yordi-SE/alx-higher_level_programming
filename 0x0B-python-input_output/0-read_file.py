#!/usr/bin/python3
"""This module conatains the defination
 of function that read text file
 """


def read_file(filename=""):
    """This is the body of the function
    """
    with open(filename, encoding='utf-8') as my_file:
        print(my_file.read(), end="")
