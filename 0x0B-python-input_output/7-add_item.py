#!/usr/bin/python3
""" Module that adds all arguments to a Python list, and then
save them to a file
"""
from sys import argv
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

try:
    f = "add_item.json"
    obj = load_from_json_file(filename)
except Exception:
    obj = []

for i in range(1, len(argv)):
    obj.append(argv[i])

with open(filename, 'w') as f:
    json.dump(obj, f)
