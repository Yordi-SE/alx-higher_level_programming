#!/usr/bin/python3
"""
This is a Module that contains the defination of
function that we use to divide each elemnts of matrix
"""


def matrix_divided(matrix, div):
    """Here we put a defination of the fuction
    """
    list1 = []
    m = "matrix must be a matrix"
    n = " (list of lists) of integers/floats"
    if matrix is None or matrix == [] or matrix == [[]]:
        raise TypeError("{}{}".format(m, n))
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("{}{}".format(m, n))
        if len(i) == 0:
            raise TypeError("{}{}".format(m, n))
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("{}{}".format(m, n))
        tmp = len(matrix[0])
        if (tmp != len(i)):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        list1 += [list(map(lambda x: round(x / div, 2), i))]
    return list1
