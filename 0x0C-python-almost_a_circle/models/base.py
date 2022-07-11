#!/usr/bin/python3
"""Python module for class Base"""


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
