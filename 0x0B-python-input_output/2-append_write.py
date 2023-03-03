#!/usr/bin/python3
"""This module contains the defination of
 function that append text to text file
 """


def append_write(filename="", text=""):
    """Here the body of the function
    """
    with open(filename, 'a', encoding='utf-8') as my_file:
        return my_file.write(text)
