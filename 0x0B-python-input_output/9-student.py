#!/usr/bin/python3
"""
Write a class Student
"""


class Student:
    """class student body"""

    def __init__(self, first_name, last_name, age):
        """
        Args:
            first_name(str): first name of student
            last_name(str): last name of student
            age(int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance
        (same as 8-class_to_json.py)"""
        return self.__dict__
