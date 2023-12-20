#!/usr/bin/python3
""" Rotates a 2D matrix """


def rotate_2d_matrix(matrix):
    """ Rotates to 90 degrees clockwise """
    matrix.reverse()
    matrix_len = len(matrix)

    for i in range(matrix_len):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
