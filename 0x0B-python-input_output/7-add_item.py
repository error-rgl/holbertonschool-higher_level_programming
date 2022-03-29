#!/usr/bin/python3
""" Module that adds all arguments to a Python list, and then
save them to a file
"""
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    arglist = load_from_json_file("add_item.json")
except FileNotFoundError:
    arglist = []

arglist += argv[1:]
save_to_json_file(arglist, "add_item.json")
