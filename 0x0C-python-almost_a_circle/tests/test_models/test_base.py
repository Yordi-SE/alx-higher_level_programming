#!/usr/bin/python3
"""This module contains
    the unittest for the class base class
    """
import unittest
from models.base import Base


class TestCaseBase(unittest.TestCase):
    
    def test_value(self):
        Ba = Base()
        self.assertEqual(Ba.id, 1)
        Ba1 = Base("You")
        self.assertEqual(Ba1.id, "You")
        Ba2 = Base()
        self.assertEqual(Ba2.id, 2)
if __name__ == '__main__':
    unittest.main()
