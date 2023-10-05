#!/usr/bin/python3
if __name__ = "__main__":
    import sys

    sum_total = 0
    length = len(sys.argv) - 1

    for a in range(length):
        sum_total += int(sys.argv[a + 1])
    print("{}".format(sum_total))
