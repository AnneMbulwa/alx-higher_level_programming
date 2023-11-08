#!/usr/bin/python3
"""
function that returns a list of lists of integers representing
the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """
    Args:
        n(int):
    """
    if n <= 0:
        return []

    x = []
    for a in range(n):
         row = []
         for b in range(1, a):
             if b == 0 or b == a:
                 row.append(1)
             else:
                 row.append(x[a - 1][b - 1] + x[a - 1][b])
                 x.append(row)
    return x
