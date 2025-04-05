#!/usr/bin/python3
"""
This module contains the matrix_divided function.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists): The matrix to divide. Must contain only integers/floats.
        div (int or float): The number to divide by. Must not be 0.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if rows are not of the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        A new matrix with all elements divided by div and rounded to 2 decimal places.
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]

