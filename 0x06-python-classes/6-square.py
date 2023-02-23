#!/usr/bin/python3
"""This is the square class that defines a square
"""


class Square:
    """Now we have defined the square class
    """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
        for i in range(2):
            if not isinstance(position[i], int) or position[i] < 0:
                raise TypeError("position must be a tuple of 2 positive intger")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive intger")
        self.position = position

    def area(self):
        return self.__size**2

    def my_print(self):
        if (self.__size != 0):
            if self.__position[1] != 0:
                for i in range(self.__position[0]):
                    print("_", end="")
            else:
                for i in range(self.__position[0]):
                    print(" ", end="")
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def positon(self, value):
        for i in range(2):
            if not isinstance(value[i], int) or value[i] < 0:
                raise TypeError("position must be a tuple of 2 positive intger")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive intger")
        self.__position = value
