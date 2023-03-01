#!/usr/bin/python3
"""This module contains the defination
of Rectangle class
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Here we put the
    defination of the class
    """
    def __init__(self, width, height):
        """Here we define child
        constructor
        """
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
