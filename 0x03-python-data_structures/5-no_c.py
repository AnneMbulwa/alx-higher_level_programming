#!/usr/bin/env python3
def no_c(my_string):
    a = ""
    for x in range(len(my_string)):
        if (my_string[x] != 'c' and my_string[x] != 'C'):
            a += my_string[x]
    return a
