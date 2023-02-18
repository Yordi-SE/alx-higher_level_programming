#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if (ord(str[i]) > 96 and ord(str[i]) < 123):
            list1 = chr(ord(str[i]) - 32)
        else:
            list1 = str[i]
        print("{}".format(list1), end="")
    print("{}".format(""))
