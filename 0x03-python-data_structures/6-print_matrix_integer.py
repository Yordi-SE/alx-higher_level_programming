#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for num in matrix:
        for x in num:
            if (x == num[len(num) - 1]):
                print("{:d}".format(x), end="")
            else:
                print("{:d} ".format(x), end="")
        print("")
