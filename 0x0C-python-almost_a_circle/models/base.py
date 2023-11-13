#!/usr/bin/python3
import json
import csv

"""creating a class base"""

class Base:
    """class base body
    Args:
        __nb_objects(private): private instance
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Args:
            id(int): id should be an integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries(list):
            checks if list_sictionaries is none or empty
        """
        if list_dictionaries is None or len(list_dictionaries) == []:
            return ("[]")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        Args:
            The filename must be: <Class name>.json
            must use the static method
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as myjsonfile:
            if list_objs is None:
                myjsonfile.write("[]")
            else:
                lists_d = [i.to_dictionary] for i in list_objs
                json.write(Base.to_json_string(lists_d))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create a Rectangle or Square instance with “dummy”
        mandatory attributes
        use the update instance method
        Args:
            **dictionary(dict):
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        Args:
            filename must be: <Class name>.json
            must use from_json_string and create
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as myfile:
                lists_d = Base.from_json_string(myfile.read())
                instance = [cls.create(**diction) for diction in lists_d]
                return instance
        except FileNotFoundError:
            return []
