#!/usr/bin/python3
a = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - a)), end=" ")
    if a == 0 a = 32 else 0
