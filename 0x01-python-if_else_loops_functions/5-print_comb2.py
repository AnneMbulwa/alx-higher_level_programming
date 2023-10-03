#!/usr/bin/python3
"""
a program that prints numbers from 0 to 99.
"""
for nums in range(0, 100):
    if nums < 99:
        print("{:02d}.format(nums)," end=", ")
    else:
        print("\n")
