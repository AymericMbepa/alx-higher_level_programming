#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """finds all multiples of 2 in a list."""
    if len(my_list) is 0 or my_list is None:
        return None
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
