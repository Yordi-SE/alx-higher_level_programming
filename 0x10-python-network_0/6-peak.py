#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """here we write
    body of the function"""
    length = len(list_of_integers)
    if length == 0:
        return None
    lis = sorted(list_of_integers)
    return lis[length - 1]
