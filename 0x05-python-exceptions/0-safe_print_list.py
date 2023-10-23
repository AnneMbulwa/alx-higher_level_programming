#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    for a in range(0, x):
        try:
            print(my_list[a], end=" ")
        except IndexError:
            num += 1
            break
    print()
    return (num)
