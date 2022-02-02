#!/usr/bin/python3
"""
7. Load, add, save
"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

load = load_from_json_file("add_item.json")
save_to_json_file(load + argv[1:], "add_item.json")
