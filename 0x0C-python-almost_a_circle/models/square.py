#!/usr/bin/python3
"""This module contain defination
of class called Square class
"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Here we put the defination
    of body of the class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """This is the constructor
        of the class
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """This is the magic
        function
        """
        m = "[Square] {} {}/{} - {}"
        return m.format(self.id, self.x, self.y, self.width)
