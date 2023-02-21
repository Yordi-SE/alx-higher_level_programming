#!/usr/bin/python3


def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    list1 = list(roman_string)
    if roman_string:
        for i, j in enumerate(list1):
            if (j == 'I' and (i + 1) < len(list1) and list1[i+1] != 'I'):
                if (list1[i+1] == 'V' or list1[i+1] == 'X'):
                    num = num + (my_dict[list1[i + 1]] - 1)
                    del list1[i+1]
                else:
                    continue
            else:
                num = num + my_dict[j]
    return num
