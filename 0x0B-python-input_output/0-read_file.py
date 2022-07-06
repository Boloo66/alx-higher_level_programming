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


if __name__ == "__main__":
    read_file = __import__('0-read_file').read_file
    read_file("tests/my_file_1.txt")
