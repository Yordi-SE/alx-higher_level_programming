#!/usr/bin/python3
"""This module contains defination
    of a function
    """


def append_after(filename="", search_string="", new_string=""):
    """here we put body of the
        function
        """
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(filename, 'r', encoding='utf-8') as f:
        str_r = f.readline()
        t = f.tell()
        s = len(new_string)
        m = 0
        while str_r:
            if search_string in str_r and search_string != "":
                content1 = content[:t] + new_string + content[t:]
                content = content1
                m += 1
            str_r = f.readline()
            t = (m * s) + f.tell()
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content1)
