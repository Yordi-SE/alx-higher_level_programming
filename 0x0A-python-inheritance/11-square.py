#!/usr/bin/python3
"""This module contains the
defination of class that called Square
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Here we define the class
    """
    def __init__(self, size):
        """Here we define the constructor of the class
        """
        super().integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Implement area
        """
        return self.__size**2

    def __str__(self):
        """magic str method
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
