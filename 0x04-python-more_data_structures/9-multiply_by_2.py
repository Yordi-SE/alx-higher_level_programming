#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    list1 = []
    for i, v in a_dictionary.items():
        list1 = list1 + [(i, v*2)]
    return dict(list1)
