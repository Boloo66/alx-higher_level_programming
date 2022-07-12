#!/usr/bin/python3
"""Python module for class Base"""
import json


class Base:
    """An empty base class template
    Args:
        id(int): can be None else the value given is assigned to id"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor function for class Base"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """dump python object to json"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        string = json.dumps(list_dictionaries)
        return string

    @classmethod
    def save_to_file(cls, list_objs):
        """converts python obj to json string"""
        """Write the JSON serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))
