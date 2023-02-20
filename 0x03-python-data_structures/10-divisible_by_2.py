#!//usr/bin/python3


def divisible_by_2(my_list=[]):
    list1 = []
    list2 = [True]
    list3 = [False]
    for i in my_list:
        if (i % 2 == 0):
            list1 = list1 + list2
        else:
            list1 = list1 + list3
    return list1
