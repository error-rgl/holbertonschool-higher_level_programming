#!/usr/bin/python3
""" Module that adds all arguments to a Python list, and then
save them to a file
"""
import sys
import json

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

list_arg = []

try:
    with open("add_item.json", "r") as file:
        list_arg = json.loads(file.read())
except FileNotFoundError:
    pass
finally:
    with open("add_item.json", "w") as file:
        for pos in range(1, len(sys.argv)):
            list_arg.append(sys.argv[pos])
        file.write(json.dumps(list_arg))
