#!/usr/bin/python3
"""This module contains the defination
of class MyInt that inherite from int
"""


class MyInt(int):
    """Here we put the defination
    """
    def __eq__(self, other):
        """Here we put the defination
        """
        if self.real == other.real:
            return False
        return True

    def __ne__(self, other):
        """here we put the defination
        """
        if self.real != other.real:
            return False
        return True
