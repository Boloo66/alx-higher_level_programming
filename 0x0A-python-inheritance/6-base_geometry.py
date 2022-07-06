#!/usr/bin/python3
"""This is a template for a base geometry class in python"""


class BaseGeometry:
    """A class for the BaseGeometry"""

    def area(self):
        """Empty initializer for class"""
        raise Exception("area() is not implemented")

    def __getattribute__(self, __name: str) -> None:
        """Magic attribute method"""
        raise Exception("area() is not implemented")
