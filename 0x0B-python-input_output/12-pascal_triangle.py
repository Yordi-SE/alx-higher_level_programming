#!/usr/bin/python3
"""This module contains the defination of
     the function that returns pascal
     triangle
     """


def pascal_triangle(n):
    """here we put the body of
    the function
    """
    if n <= 0:
        return []
    list1 = [[1], [1, 1]]
    list3 = [1]
    if n <= 2:
        if n == 1:
            return [[1]]
        return list1
    for w in range(n - 2):
        list2 = list1[len(list1) - 1]
        for u, i in enumerate(list2):
            try:
                list3.append(list2[u] + list2[u + 1])
            except Exception:
                break
        list3.append(1)
        list1.append(list3)
        list3 = [1]
    return list1
