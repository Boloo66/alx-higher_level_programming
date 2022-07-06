#!/usr/bin/python3
"""This is a template for a base geometry class in python"""


class BaseGeometry:
    """A class for the BaseGeometry"""

    def __init__(self) -> None:
        """Empty initializer for class"""
        pass

    def __getattribute__(self, __name: str) -> None:
        raise Exception("area() is not implemented")
