#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    simple_matrix = matrix.copy()

    for c in range(len(matrix)):
        simple_matrix[c] = list(map(lambda n: n**2, matrix[c]))

    return (simple_matrix)
