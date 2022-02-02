#!/usr/bin/python3
"""
13. Search and update
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each line containing a string
    """
    new_cont = ""
    with open(filename, 'r+', encoding="utf-8") as f:
        for line in f:
            new_cont += line
            if search_string in line:
                new_cont += new_string
        f.seek(0)
        f.write(new_cont)
