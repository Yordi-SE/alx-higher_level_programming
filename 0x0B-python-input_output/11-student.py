#!/usr/bin/python3
"""This module contains the defination of
    class Student
    """


class Student:
    """Here is the body of the function
    """
    def __init__(self, first_name, last_name, age):
        """here we put the constructor of the
        class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """here we put that retrieves
        a dictionary of self
        """
        try:
            my_dict = {}
            if all(isinstance(i, str) for i in attrs):
                for i in attrs:
                    if i in self.__dict__.keys():
                        my_dict[i] = self.__dict__[i]
                return my_dict
        except Exception:
            pass
        return self.__dict__

    def reload_from_json(self, json):
        """here we put that replaces
        the attributes of the instance
        """
        for i in json:
            self.__dict__[i] = json[i]
