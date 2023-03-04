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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This is puplic instance method
        that returns the area of the
        rectangle
        """
        return self.width * self.height

    def display(self):
        """This puplic instance method prints
        the instance to stdout by #
        """
        for u in range(self.y):
            print("")
        for y in range(self.height):
            for t in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """This is magic method
        that returns string
        """
        m = "[Rectangle] ({}) {}/{} - {}/{}"
        return m.format(self.id, self.x, self.y, self.width, self.height)

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

    def to_dictionary(self):
        my_dict = {}
        my_dict['width'] = self.width
        my_dict['height'] = self.height
        my_dict['x'] = self.x
        my_dict['y'] = self.y
        my_dict['id'] = self.id
        return my_dict
