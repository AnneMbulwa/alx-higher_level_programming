#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for a in range(0, x):
        try:
            print("{:d}".format(my_list), end=" ")
            num += 1
        except (ValueError, IndexErrror):
            pass
    print()
    return (num)
