#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        s = dict(sorted(a_dictionary.items(), key=lambda item: item[1]))
        for i in s.keys():
            continue
        return i
