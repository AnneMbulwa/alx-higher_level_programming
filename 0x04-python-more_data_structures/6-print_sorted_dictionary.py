#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_order = sorted(a_dictionary.keys())
    for key in list_order:
        print("{}:{}".format(key, a_dictionary(key))
