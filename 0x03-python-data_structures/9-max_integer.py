#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    biggest = my_list.copy()
    biggest.sort()
    return biggest[-1]
