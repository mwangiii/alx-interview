#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    p = []

    if n <= 0:
        return p

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(p[i - 1][j] + p[i - 1][j - 1])
        p.append(row)

    return p
