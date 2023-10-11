#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    score_av = 0
    weight_av = 0

    for tuptotal in my_list:
        score_av += tuptotal[0] * tuptotal[1]
        weight_av += tuptotal[1]

    return (score_av / weight_av)
