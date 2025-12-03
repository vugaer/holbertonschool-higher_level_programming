#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for cols in range(len(matrix)):
        for rows in range(len(cols)):
            print("{:d}".format(matrix[cols][rows]), end=' ')
        print()
