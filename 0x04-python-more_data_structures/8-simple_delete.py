#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    a_dictionary[key] = 2
    del a_dictionary[key]
    return a_dictionary
