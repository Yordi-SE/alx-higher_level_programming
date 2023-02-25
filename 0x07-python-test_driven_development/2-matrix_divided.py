#!/usr/bin/python3


def matrix_divided(matrix, div):
    list1 = []
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
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
