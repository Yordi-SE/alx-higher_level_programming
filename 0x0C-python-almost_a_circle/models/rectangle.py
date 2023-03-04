#!/usr/bin/python3
"""This module contains the defination
of the class Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """HEre we put body
    of the class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """This is the constructor
        of this class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """This getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """This is setter
        """
        self.__width = value

    @property
    def height(self):
        """This is getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """This is setter
        """
        self.__height = value

    @property
    def x(self):
        """This is getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """This is setter
        """
        self.__x = value

    @property
    def y(self):
        """This is getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """This is setter
        """
        self.__y = value