#!/usr/bin/python3
"""
function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Description:
        matrix must be a list of lists of integers or floats
        Each row of the matrix must be of the same size
        div must be a number (integer or float)
        div can’t be equal to 0
        All elements of the matrix should be divided by div,
        rounded to 2 decimal places
     Raises:
            TypeErrors
            Zerodivision Error
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(col, int) or isinstance(col, float))
                    for col in [a for row in matrix for a in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda y: round(y / div, 2), row)) for row in matrix)
