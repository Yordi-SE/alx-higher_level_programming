#!/usr/bin/python3
"""This module contain the unit
test for the class rectangle
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_width(self):
        r2 = Rectangle(4, 5)
        r2.width = 6
        self.assertEqual(r2.width, 6)
        with self.assertRaises(ValueError):
            r2.width = -1
        with self.assertRaises(TypeError):
            r2.width = 'str'
        with self.assertRaises(TypeError):
            r2.width = True
        with self.assertRaises(ValueError):
            r2.width = 0

    def test_height(self):
        r3 = Rectangle(4, 5)
        r3.height = 6
        self.assertEqual(r3.height, 6)
        with self.assertRaises(ValueError):
            r3.height = -1
        with self.assertRaises(TypeError):
            r3.height = True
        with self.assertRaises(ValueError):
            r3.height = 0

    def test_x(self):
        r4 = Rectangle(4, 5)
        r4.x = 7
        self.assertEqual(r4.x, 7)
        with self.assertRaises(ValueError):
            r4.x = -1
        with self.assertRaises(TypeError):
            r4.x = True

    def test_y(self):
        r6 = Rectangle(4, 5)
        self.assertEqual(r6.y, 0)
        r6.y = 7
        self.assertEqual(r6.y, 7)
        r7 = Rectangle(4, 5, y=5)
        self.assertEqual(r7.y, 5)
        with self.assertRaises(ValueError):
            r7.y = -1
        with self.assertRaises(TypeError):
            r7.y = True

if __name__ == "__main__":
    unittest.main()
