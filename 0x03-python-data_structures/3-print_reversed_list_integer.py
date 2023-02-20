#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list:
        list1 = my_list.copy()
        list1.reverse()
        for i in list1:
            print("{:d}".format(i))
