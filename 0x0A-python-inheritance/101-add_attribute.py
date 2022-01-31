#!/usr/bin/python3
"""
13. Can I?
"""


def add_attribute(x, y, z):
    """
    function that adds a new attribute to an object if it’s possible
    """
    if hasattr(x, "__dict__"):
        setattr(x, y, z)
    else:
        raise TypeError("can't add new attribute")
