#!/usr/bin/python3
"""This module writes to a file using JSON rep"""
import json


def save_to_json_file(my_obj, filename):
    """This fuction deserializes a json file.
    Args:
    my_obj: python object.
    filename: name of th file(.json)
    """
    with open(filename, "w+", enconding="utf-8") as f_obj:
        return (json.dump(my_obj, f_obj, indent=2, sort_keys=True))
