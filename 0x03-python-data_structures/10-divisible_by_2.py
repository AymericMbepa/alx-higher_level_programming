#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """finds all multiples of 2 in a list."""
    if len(my_list) == 0:
        return None
    new_list = []
    for i in range(len(my_list)):
        new_list.append(False)
    for i in my_list:
        if i % 2 == 0:
            new_list[i] = True
    return new_list
