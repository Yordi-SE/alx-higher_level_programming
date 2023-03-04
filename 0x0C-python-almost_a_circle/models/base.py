#!/usr/bin/python3
"""This module contains the defination
of the class Base
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """This static method returns
        the json representation a list
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
