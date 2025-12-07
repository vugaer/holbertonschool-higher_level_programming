#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    final_matrix = []
    for i in matrix:
        final_matrix += [list(map(lambda x: x**2, i))]
    return final_matrix
