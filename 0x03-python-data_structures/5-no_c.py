#!/usr/bin/env python3
def no_c(my_string):
    new_string = ""
    for x in range(len(my_string)):
        if (my_string[x] != 'c' and my_string[x] != 'C'):
            new_string += my_string[x]
    return new_string
