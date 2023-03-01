#!/usr/bin/python3
"""Here in This module My_list class which inherite
    from list class is defined
    """


class MyList(list):
    """Here the body of the class
    is defined
    """

    def print_sorted(self):
        list1 = self.copy()
        list1.sort()
        print(list1)
