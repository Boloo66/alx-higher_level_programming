#!/usr/bin/python3.9

def search_replace(my_list, search, replace):
    result = [replace if elements ==
              search else elements for elements in my_list]
    return result


my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)
print(new_list)
