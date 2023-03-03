#!/usr/bin/python3
"""This module contains the defination of
 function that returns JSON representation
 """
import json


def save_to_json_file(my_obj, filename):
    """Here is the body of
    the function
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
