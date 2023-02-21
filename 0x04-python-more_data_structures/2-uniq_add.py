#!/usr/bin/python3


def uniq_add(my_list=[]):
    set1 = set(my_list)
    summ = 0
    for i in set1:
        summ = summ + i
    return summ
