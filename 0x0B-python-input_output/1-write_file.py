#!/usr/bin/python3
"""This Module contains the defination of
 function
 """


def write_file(filename="", text=""):
    """Here is the body of the function
    """
    with open(filename, 'w', encoding='utf-8') as my_file:
        return my_file.write(text)
