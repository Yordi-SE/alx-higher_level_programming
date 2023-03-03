#!/usr/bin/python3
"""This module contains the defination of
 function that returns JSON representation
 """
import json


def load_from_json_file(filename):
    """Here is the body of
    the function
    """
    with open(filename, encoding='utf-8') as f:
        return json.loads(f.read())
