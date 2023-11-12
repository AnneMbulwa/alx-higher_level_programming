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

    x = [[1]]
    while len(x) != n:
        col = x[-1]
        row = [1]
        for b in range(len(col) - 1):
            row.append(col[b] + col[b + 1])
        row.append(1)
        x.append(row)
    return x
