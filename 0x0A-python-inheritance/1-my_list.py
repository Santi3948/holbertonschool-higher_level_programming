#!/usr/bin/python3
"""1. My list"""


"""My list class"""


class MyList(list):
    """print sorted"""
    def print_sorted(self):
        for item in self:
            if type(item) != int:
                raise TypeError("must be a list of integers")
        print(sorted(self))
