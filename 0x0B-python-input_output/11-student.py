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

    def to_json(self, attrs=None):
        """
        Args:
            that retrieves a dictionary representation of a
            Student instance (same as 8-class_to_json.py):

            If attrs is a list of strings, only attribute
            names contained in this list must be retrieved.
            Otherwise, all attributes must be retrieved
        """
        if attrs is None:
            return self.__dict__
        else:
            return {ke: getattr(self, ke)
                    for ke in attrs if hasattr(self, ke)}

    def reload_from_json(self, json):
        """
        Args:
            that replaces all attributes of the Student instance
        """
        for ke, val in json.items():
            setattr(self, ke, val)
