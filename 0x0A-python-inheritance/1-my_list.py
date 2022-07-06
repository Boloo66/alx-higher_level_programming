#!/usr/bin/python3
"""Module that inherites from python list class"""


class MyList(list):
    """MyList class that inherits from list and print list object in sorted order"""

    def print_sorted(self):
        """Function that prints list in sorted order"""
        print(sorted(self))


if __name__ == "__main__":
    MyList = __import__('1-my_list').MyList

    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
