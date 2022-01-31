#!/usr/bin/python3
"""
1. My list
"""


class MyList(list):
    """
    MyList class
    """
    def print_sorted(self):
        for item in self:
            if type(item) != int:
                raise TypeError("must be a list of integers")
        print(sorted(self))
