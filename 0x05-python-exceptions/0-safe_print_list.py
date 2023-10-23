#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    for a in range(x):
        try:
            print(f"{my_list[a]}", end=" ")
        except IndexError:
            num += 1
            break
    print()
    return (num)
