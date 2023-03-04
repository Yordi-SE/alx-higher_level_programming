#!/usr/bin/python3
"""This module contain the unit
test for the class rectangle
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    
    def test_id(self):
        r = Rectangle(4, 5)
        self.assertEqual(r.id, 4)
        r1 = Rectangle(4, 5, id='YOU')
        self.assertEqual(r1.id, 'YOU')

    def test_width(self):
        r2 = Rectangle(4, 5)
        self.assertEqual(r2.width, 4)
        r2.width = 5
        self.assertEqual(r2.width, 5)

    def test_height(self):
        r3 = Rectangle(4, 5)
        self.assertEqual(r3.height, 5)
        r3.height = 6
        self.assertEqual(r3.height, 6)

    def test_x(self):
        r4 = Rectangle(4, 5)
        self.assertEqual(r4.x, 0)
        r4.x = 7
        self.assertEqual(r4.x, 7)
        r5 = Rectangle(4, 5, x=5)
        self.assertEqual(r5.x, 5)

    def test_y(self):
        r6 = Rectangle(4, 5)
        self.assertEqual(r6.y, 0)
        r6.y = 7
        self.assertEqual(r6.y, 7)
        r7 = Rectangle(4, 5, y=5)
        self.assertEqual(r7.y, 5)

if __name__ == "__main__":
    unittest.main()
