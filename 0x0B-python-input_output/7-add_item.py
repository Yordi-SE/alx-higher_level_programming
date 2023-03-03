#!/usr/bin/python3
"""This is script adds list ot json
    file
    """
import sys
import json
import os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
try:
    mylist = load_from_json_file("add_item.json")
except Exception:
    mylist = []
for i in sys.argv:
    if i != sys.argv[0]:
        mylist += [i]
save_to_json_file(mylist, "add_item.json")
