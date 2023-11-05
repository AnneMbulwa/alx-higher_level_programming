#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    biggest = my_list[0]
    for a in range(len(my_list)):
        if a > biggest:
            biggest = a
    return biggest
