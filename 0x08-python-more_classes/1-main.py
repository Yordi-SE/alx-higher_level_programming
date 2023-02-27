#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
m3 = Rectangle(1, 2.3)
print(m1.height)
print(m2.width)
print(m3.width, m3.height)
