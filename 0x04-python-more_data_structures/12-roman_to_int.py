#!/usr/bin/python3


def roman_to_int(roman_string):
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    if roman_string:
        for i in my_dict.keys():
            for j in roman_string:
                if (i == j):
                    num = num + my_dict[i]
    return num
