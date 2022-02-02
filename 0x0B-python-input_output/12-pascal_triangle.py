#!/usr/bin/python3
"""
12. Pascal's Triangle
"""



def pascal_triangle(n):
	"""
	Returns a list of lists of integers representing the Pascal’s triangle of n
	"""
    lis = []
    if n <= 0:
        return lis
    lis_aux = [1]
    lis.append(lis_aux)
    if n = 1:
        return lis
    if 
