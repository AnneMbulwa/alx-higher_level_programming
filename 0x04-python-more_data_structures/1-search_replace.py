#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    newly_list = my_list[:]

    for index, a in enumerate(newly_list):
        if a == search:
            newly_list[index] = replace
    return (newly_list)
