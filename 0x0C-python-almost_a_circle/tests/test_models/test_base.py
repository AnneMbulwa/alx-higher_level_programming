#!/usr/bin/python3
"""unittest for models/test_base.py"""

import os
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.Testcase):
    """testing the base class"""

    def setUp(self):
        """testing for instances of base class"""
        Base._Base__nb_objects = 0
        pass

    """test for the attributes(id)"""
    def test_ids(self):
        """checks if ids match with values given"""
        b0 = Base()
        self.assertEqual(b0.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b3 = Base(100)
        self.assertEqual(b3.id, 100)
        b4 = Base(-7)
        self.assertEqual(b4.id, -7)
        b5 = Base(6)
        self.assertEqual(b5.id, 6)

    def test_type(self):
        """tests the type and instance of id attributes"""
        b5 = Base()
        self.assertEqual(type(b5), Base)
        self.assertTrue(isinstance(b5, Base))
    
    def test_nb_instances_private(self):
        """tests if nb_object instances are private or not"""
        with self.assertRaises(AttributeError):
            print(Base().__nb_instances)

    def test_id_public(self):
        """tests the ids if public"""
        b = Base(12)
        b.id = 55
        self.assertEqual(55, b.id)

    def test_str_id(self):
        """tests if id attr is a string"""
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        """tests if id attribute is a float"""
        self.assertEqual(6.5, Base(6.5).id)

    """test the class"""
    def test_class(self):
        """tests if the class is base"""
        self.assertTrue(Base(100), self.__class__ == Base)

    """test the args"""
    def test_args(self):
        with self.assertRaises(TypeError):
            Base(50, 50)

"""testing to_json string method in base class"""
class TestBase_to_json_string(unittest.TestCase):

    def test_to_json_string_type(self):
        r = [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}]
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string(self):
        r1 = [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}]
        r2 = [{"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]
        lists_d = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(lists_d)))

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

"""Testing from json string to python object"""
class TestBase_from_json_string:

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)
    
    def test_create(self):
        """testing new instance dictionary"""
        r1 = Rectangle(3, 5, 1, 2, 99)
        rdict = r1.to_dictionary()
        r2 = Rectangle.create(**rdict)
        self.assertEqual(str(r1), '[Rectangle] (99) 1/2 - 3/5')
        self.assertEqual(str(r2), '[Rectangle] (99) 1/2 - 3/5')
        self.assertIsNot(r1, r2)

    def test_save_to_file(self):
        """Test save to file"""
        r1 = Rectangle(10, 7, 2, 8, 99)
        r2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as myfile:
            self.assertEqual(
                json.dumps([r1.to_dictionary(), r2.to_dictionary()]),
                myfile.read())

    def test_save_none_to_file(self):
        """Test save None to file"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as myfile:
            self.assertEqual('[]', myfile.read())

    def test_empty_none_to_file(self):
        """Test save empty list to file"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as myfile:
            self.assertEqual('[]', myfile.read())

    def test_load_from_file(self):
        """Test load from file"""
        r1 = Rectangle(10, 7, 2, 8, 99)
        r2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([r1, r2])
        rects = Rectangle.load_from_file()
        self.assertEqual(len(rects), 2)
        for k, x in enumerate(rects):
            if k == 0:
                self.assertEqual(str(x), '[Rectangle] (99) 2/8 - 10/7')
            if k == 1:
                self.assertEqual(str(x), '[Rectangle] (98) 2/2 - 2/4')

    def test_load_from_none_file(self):
        """Test load from None file"""
        Rectangle.save_to_file(None)
        rects = Rectangle.load_from_file()
        self.assertEqual(type(rects), list)
        self.assertEqual(len(rects), 0)

    def test_load_from_empty_file(self):
        """Test load from empty file"""
        Rectangle.save_to_file([])
        rects = Rectangle.load_from_file()
        self.assertEqual(type(rects), list)
        self.assertEqual(len(rects), 0)

if __name__ == "__main__":
    unittest.main()
