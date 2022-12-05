#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """adds 2 tuples"""
    na = len(tuple_a)
    nb = len(tuple_b)
    if na < 2:
        if na == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if nb < 2:
        if nb == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0
    return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
