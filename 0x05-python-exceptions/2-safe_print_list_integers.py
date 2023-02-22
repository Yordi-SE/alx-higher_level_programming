#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num += 1
        except OverflowError:
            pass
        except ValueError:
            pass
        except TypeError:
            pass
    if (x > 0):
        print("")
    return num
