#!/usr/bin/python3
def roman_to_int(roman_string):
    if not instance(roman_string, str):
        return 0
    if not roman_string:
        return 0
    roman_digits = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
            }
    value = 0
    total = 0
    for a in reversed(roman_string):
        val = roman_numerals.get(a, 0)
        if val < value:
            total -= val
        else:
            total += val
        value = val

    return total
