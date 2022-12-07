#!/usr/bin/python3
def common_elements(set_1, set_2):
    """returns a set of common elements in two sets"""
    common = []
    for x in set_1:
        for y in set_2:
            if x == y:
                common.append(x)
    return common
