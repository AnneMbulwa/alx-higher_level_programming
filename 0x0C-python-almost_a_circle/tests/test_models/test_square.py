#!/usr/bin/python3
"""Unittest for class square"""

import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_all_attributes_given(self):
        """tests if all attributes are provided"""
        s0 = (4, 5, 3, 2)
        """height == width == size"""
        self.assertTrue(s0.width == 4)
        self.assertTrue(s0.height == 4)
        self.assertTrue(s0.size == 4)
        self.assertTrue(s0.x == 5)
        self.assertTrue(s0.y == 3)
        self.assertTrue(s0.id == 2)

    def test_not_all_attributes_given(self):
        """tests if all attributes are not provided"""
        s1 = (6, 8)
        self.assertTrue(s1.width == s1.height == s1.size == 6)
        self.assertTrue(s1.x == 8)
        self.assertTrue(s1.y == 0)
        self.assertTrue(si.id is not None)

    """test class"""
    def test_class(self):
        s = Square(5)
        self.assertEqual(type(s), Square)

    def test_inhertance(self):
        """test if square inherits from class rectangle or class base"""
        s1 = Square(5)
        self.assertTrue(isinstance(s1, Rectangle))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertFalse(isinstance(Square, Rectangle))
        self.assertTrue(isinstance(s1, Base))
        self.assertTrue(issubclass(Square, Base))
        self.assertFalse(isinstance(Square, Base))

    def test_attributes_values(self):
        with self.assertRaises(TypeError) as f:
            s = Square("Hi", 2)
        self.assertEqual("width must be an integer", str(f.exception))
        with self.assertRaises(TypeError) as f:
            s = Square(2, "World")
        self.assertEqual("x must be an integer", str(f.exception))
        with self.assertRaises(TypeError) as f:
            s = Square(4, 2, "Fall", 3)
        self.assertEqual("y must be an integer", str(f.exception))
        with self.assertRaises(ValueError) as f:
            s = Square(0, 2)
        self.assertEqual("width must be > 0", str(f.exception))
        with self.assertRaises(ValueError) as f:
            s = Square(-2)
        self.assertEqual("width must be > 0", str(f.exception))
        with self.assertRaises(ValueError) as f:
            s = Square(2, -3)
        self.assertEqual("x must be >= 0", str(f.exception))
        with self.assertRaises(ValueError) as f:
            s = Square(2, 5, -2, 6)
        self.assertEqual("y must be >= 0", str(f.exception))

    def test_args(self):
        with self.assertRaises(TypeError):
            """arguments are too many"""
            Square(9, 10, 7, 4, 3, 5)
        with self.assertRaises(TypeError):
            """arguments are too less or none"""
            Square()
            Square(None)

    def test_area(self):
        s1 = Square(2)
        self.assertEqual(s1.area(), 4)
        s1 = Square(4, 0, 0, 0)
        self.assertEqual(s1.area(), 16)

    def test_display(self):
        """Test method: display"""
        with StringIO() as f, redirect_stdout(f):
            Square(4).display()
            b = f.getvalue()
        self.assertEqual(b, '####\n####\n####\n####\n')
        with StringIO() as f, redirect_stdout(f):
            Square(3, 1, 2).display()
            b = f.getvalue()
        self.assertEqual(b, '\n\n ###\n ###\n ###\n')

    def test_print(self):
        """Test method: __str__"""
        s2 = Square(1, 32, 3, 49)
        s2.size = 99
        self.assertEqual(str(s2), '[Square] (49) 32/3 - 99')

    def test_updates(self):
        """updates of *args"""
        s3 = Square(45, 20, 5, 77)
        s3.update(10, 10, 10, 10)
        self.assertEqual(str(s3), '[Square] (10) 10/10 - 10')
        s3.update(99)
        self.assertEqual(str(s3), '[Square] (99) 10/10 - 10')
        s3.update(99, 5)
        self.assertEqual(str(s3), '[Square] (99) 10/10 - 5')

        """udates of **kwargs"""
        s3.update(id=2, size=5, nize=6)
        self.assertEqual(str(s3), '[Square] (2) 20/5 - 5')

    def test_to_dictionary(self):
        """tests the method: to_dictionary"""
        sdict = Square(4, 6, 8, 10).to_dictionary()
        self.assertEqual(type(sdict), dict)
        s2 = Square(1, 1)
        s2.update(**sdict)
        self.assertEqual(str(s2), '[Square] (10) 6/8 - 4')

if __name__ == "__main__":
    unittest.main()
