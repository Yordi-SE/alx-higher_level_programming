#!/usr/bin/python3
"""This module contains the defination
of the class Base
"""


class Base:
    """Here  body of the
    class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Here we define the constructor
        of this class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
