#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ adds all unique integers in a list (only once for each integer)"""
    sum1 = 0
    sum2 = 0
    new_list = []
    for x in my_list:
        if my_list.count(x) == 1:
            sum1 += x
        else:
            new_list.append(x)
    new_list = list(set(new_list))
    for i in new_list:
        sum2 += i
    return sum1 + sum2
