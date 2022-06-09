#!/usr/bin/python3.9

def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    items = list(a_dictionary.items())
    items = [(i[1], i[0]) for i in items]
    items.sort()
    items = [(i[0], i[1]) for i in items]
    new_dict = items[-1][1]
    return new_dict


a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
