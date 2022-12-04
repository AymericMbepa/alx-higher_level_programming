#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """ prints a matrix of integers"""
    for i in range(len(matrix)):
        n = len(matrix[i])
        for j in range(n):
            if j < n - 1:
                print('{:d}'.format(matrix[i][j]), end=' ')
            else:
                print('{:d}'.format(matrix[i][j]), end='')
        print("$")
