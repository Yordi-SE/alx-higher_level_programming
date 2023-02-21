#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        sorted_dict = dict(sorted(a_dictionary.items(), key=lambda item: item[1]))
        for i in sorted_dict.keys():
            continue
        return i
