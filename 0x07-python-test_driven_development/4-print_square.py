#!/usr/bin/python3
"""Print Square
"""


def print_square(size):
    """prints a square with the character #
    """


	if !isinstance(size, int):
		raise TypeError("size must be an integer")
	if size < 0:
		raise ValueError("size must be >= 0")
	for i in range(1, size + 1):
		for j in range(1, size + 1):
			print("{}".format(j), end="")
		print()
