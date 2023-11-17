#!/usr/bin/python3
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.Testcase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_all_attribute_given(self):
        """test if all attributes(4) of the rectangle are provided"""
        r = (12, 23, 5, 4, 77)
        self.assertTrue(r.width == 12)
        self.assertTrue(r.height == 23)
        self.assertTrue(r.x == 5)
        self.assertTrue(r.y == 4)
        self.assertTrue(r.id == 77)

    def test_not_all_attr_given(self):
        """test if not all attributes are provided
        if not attributes given the missing attributes are
        set to 0 by default"""
        r1 = (34, 9)
        self.assertTrue(r1.width == 34)
        self.assertTrue(r1.height == 9)
        self.assertTrue(r1.x == 0)
        self.assertTrue(r1.y == 0)
        self.assertTrue(r1.id is not None)

    """testing class"""
    def test_class(self):
        r = (3, 4)
        self.assertEqual(type(Rectangle(r)), Rectangle)

    def test_inheritance_class(self):
        r2 = Rectangle(1, 2)
        self.assertTrue(isinstance(r2, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))

    def test_private_attritube_access(self):
        """Test private attributes are not accessible"""
        with self.assertRaises(AttributeError):
            print(Rectangle.__width)
            print(Rectangle.__height)
            print(Rectangle.__x)
            print(Rectangle.__y)

    def test_attr_values(self):
        with self.assertRaises(TypeError) as f:
            r = Rectangle("Hi", 2)
        self.assertEqual("width must be an integer", str(f.exception))
        with self.assertRaises(TypeError) as f:
            r = Rectangle(4, "World")
        self.assertEqual("height must be an integer", str(f.exception))
        with self.assertRaises(TypeError) as f:
            r = Rectangle(7, 2, "Fall", 3)
        self.assertEqual("x must be an integer", str(f.exception))
        with self.assertRaises(TypeError) as f:
            r = Rectangle(10, 2, 2, "Bar")
        self.assertEqual("y must be an integer", str(f.exception))
        with self.assertRaises(ValueError) as f:
            r = Rectangle(0, 4)
        self.assertEqual("width must be > 0", str(f.exception))
        with self.assertRaises(ValueError) as f:
            r = Rectangle(8, 0)
        self.assertEqual("height must be > 0", str(f.exception))
        with self.assertRaises(ValueError) as f:
            r = Rectangle(2, -3)
        self.assertEqual("height must be > 0", str(f.exception))
        with self.assertRaises(ValueError) as f:
            r = Rectangle(2, 5, -5, 6)
        self.assertEqual("x must be >= 0", str(f.exception))
        with self.assertRaises(ValueError) as f:
            r = Rectangle(2, 8, 19, -35)
        self.assertEqual("y must be >= 0", str(f.exception))

    """test for the number of arguments"""
    def test_args(self):
        """raises an error when too many argument encounters"""
        with self.assertRaises(TypeError):
            Rectangle(12, 4, 20, 14, 5, 9)
        """raises an error when there are too few arguments"""
        with self.assertRaises(TypeError):
            Rectangle(13)
            Rectangle()
            Rectangle(None)

    def test_area(self):
        r0 = Rectangle(3, 5)
        self.assertEqual(r0.area(), 15)
        r1 = Rectangle(13, 56)
        self.assertEqual(r1.area(), 728)
        r2 = Rectangle(2, 2, 0, 0, 5)
        self.assertEqual(r2.area(), 4)

    def test_display(self):
        """displays the test method: display"""
        with StringIO() as f, redirect_stdout(f):
            Rectangle(2, 3).display()
            b = f.getvalue()
            self.assertEqual(b, '##\n##\n##\n')
        with StringIO() as f, redirect_stdout(f):
            Rectangle(3, 5, 4, 1).display()
            b = f.getvalue()
            self.assertEqual(b, '\n\n ##\n ##\n ##\n')

    def test_print(self):
        """print __str__ test method"""
        r0 = Rectangle(5, 4, 3, 2, 1)
        self.assertEqual(str(r0), '[Rectangle] (1) 3/2 - 5/4')

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)

        r1.update(89)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 10/10')
        r1.update(89, 2)
        self.assertEqusl(str(r1), '[Rectangle] (89) 10/10 - 2/10')
        r1.update(89, 2, 5)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 2/5')
        r1.update(89, 2, 5, 7, 9)
        self.assertEqual(str(r1), '[Rectangle] (89) 7/9 - 2/5')

        """updates in *args error raises"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(99, 1, 2, 3, "stg")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(99, 1, 2, 3, -9)

        """update **kwargs"""
        r1.update(id=99)
        self.assertEqual(str(r1), '[Rectangle] (99) 10/10 - 10/10')
        r1.update(id=46, x=70, y=35, width=5)
        self.assertEqual(str(r1), '[Rectangle] (46) 70/35 - 5/10')

    def test_to_dictionary(self):
        """Test method: to_dictionary"""
        rdict = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        self.assertEqual(type(rdict), dict)
        r2 = Rectangle(10, 10)
        r2.update(**rdict)
        self.assertEqual(str(r2), '[Rectangle] (5) 3/4 - 1/2')

if __name__ == "__main__":
    unittest.main()
