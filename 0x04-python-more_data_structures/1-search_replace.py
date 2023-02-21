#!/usr/bin/python3


def search_replace(my_list, search, replace):
    list1 = []
    for a in my_list:
        if (a == search):
            list1.append(replace)
        else:
            list1.append(a)
    return list1
