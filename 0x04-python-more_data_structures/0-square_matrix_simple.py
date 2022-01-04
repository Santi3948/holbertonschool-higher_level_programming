#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        mape = map(lambda x: x * x, i)
        new_matrix.append(list(mape))
    return new_matrix
