#!/usr/bin/python3
def uppercase(str):
    for string in str:
        if ord(string) in range (97, 123):
            string = chr(ord(string) - 32)
        print("{:s}".format(string), end=" ")
    print()
