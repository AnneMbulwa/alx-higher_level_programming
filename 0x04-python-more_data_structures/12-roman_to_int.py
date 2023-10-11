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
    total = 0
    a = 0

    while a < len(roman_string):
        if a + 1 < len(roman_string) and roman_digits[roman_string[a]] < roman_digits[roman_string[a + 1]]:
            total += roman_digits[roman_string[a + 1]] - roman_digits[roman_string[a]]
            a += 2
        else:
            total += roman_digits[roman_string[a]]
            a += 1

    return (total)
