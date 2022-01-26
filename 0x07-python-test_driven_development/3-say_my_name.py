#!/usr/bin/python3
"""Prints a name
"""


def say_my_name(first_name, last_name=""):
    """Prints a name
    """

	if !isinstance(first_name, str):
		raise TypeError("first_name must be a string")
	if !isinstance(last_name, str):
		raise TypeError("last_name must be a string")
	print("My name is {:s} {:s}" .format(first_name, last_name))
