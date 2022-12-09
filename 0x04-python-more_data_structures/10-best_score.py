#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value"""
    best = 0
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    keys = list(a_dictionary)
    for val in keys:
        if a_dictionary[val] > best:
            best_val = val
            best = a_dictionary[val]
    return best_val
