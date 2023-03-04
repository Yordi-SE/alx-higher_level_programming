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

    @classmethod
    def save_to_file(cls, list_objs):
        """This class method will save
        write json representation to a file
        """
        with open("{}.json".format(cls.__name__), 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list1 = []
                for i in list_objs:
                    list1.append(i.to_dictionary())
                f.write(cls.to_json_string(list1))

    @staticmethod
    def from_json_string(json_string):
        """This static method load data
        from json string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """This class method
        returns assinged instance
        """
        if cls.__name__ == "Rectangle":
            instance = cls(4, 5)
        else:
            instance = cls(3)
        instance.update(**dictionary)
        return instance
