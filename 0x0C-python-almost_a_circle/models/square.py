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

    @property
    def size(self):
        """This is getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """This is setter
        """
        self.width = value
        self.height = value

    def __str__(self):
        """This is the magic
        function
        """
        m = "[Square] ({}) {}/{} - {}"
        return m.format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """This puplic method updates
        the attribute of the class
        """
        if not args or len(args) == 0:
            for i, j in kwargs.items():
                if i == 'id':
                    self.id = j
                if i == 'width':
                    self.width = j
                if i == 'height':
                    self.height = j
                if i == 'x':
                    self.x = j
                if i == 'y':
                    self.y = j
        else:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except Exception:
                pass
