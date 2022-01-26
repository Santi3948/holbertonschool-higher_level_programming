#!/usr/bin/python3
"""Divide a matrix
"""


def matrix_divided(matrix, div):
    """divide all elements of a matrix
    """

    new_matrix = []
	aux = []
	if !isinstance(div, int) or !isinstance(div, float):
		raise TypeError("div must be a number")
	if div == 0:
		raise ZeroDivisionError("division by zero")
	if !isinstance(matrix, list):
		raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
	if matrix[0]:
		size = len(matrix[0])
	for i in matrix:
		if !isinstance(i, list):
			raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
		if len(matrix[i]) != size:
			raise TypeError("Each row of the matrix must have the same size")
		for j in i:
			if !isinstance(j, float) or !isinstance(j, int):
				raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
			aux.append(float("{:.2f}".format(j/div)))
		new_matrix.append(aux)
	return new_matrix
