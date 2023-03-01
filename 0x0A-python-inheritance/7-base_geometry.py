#!/usr/bin/python3
"""define an empty class
BaseGeometry
"""


class BaseGeometry:
    """doc for the class
    """
    def area(self):
        """ check for area
        implementation
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator method
        """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
