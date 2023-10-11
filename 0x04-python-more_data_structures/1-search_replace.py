#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newly_list = my_list.copy()
    for element in range(len(my_list)):
        if element == search:
            newly_list.append(replace)
        else:
            newly_list.append(element)
    return (newly_list)
