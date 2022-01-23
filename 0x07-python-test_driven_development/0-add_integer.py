#!/usr/bin/python3
"""Integers addition



"""


def add_integer(a, b=98):
    """sumum of a and b

    """

    if not isinstance(a, int):
        if isinstance(a, float):
            a = int(a)
        else:
            raise TypeError("a must be an integer")

    if not isinstance(b, int):
        if isinstance(b, float):
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a+b
