#!/usr/bin/python3
"""This function reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """This function parses a txt file
    Args:
    @filename: name of the file to be parsed
    """
    if filename == "":
        raise NameError("Filename cannot be empty")

    try:
        with open(filename, encoding="utf8") as f_obj:
            buffer = f_obj.read()

    except (FileNotFoundError, NameError):
        raise FileNotFoundError("{} not found".format(filename))

    else:
        print(buffer, end="")
