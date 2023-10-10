#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """
    print the triangle
    """
    p = [[1]]

    if n <= 0:
        return []

    for i in range(1, n+1):
        row = [1]
        for j in range(1, i):
            if j == i - 1:
                row.append(1)
            else:
                row.append(p[i - 1][j] + p[i - 1][j - 1])
        p.append(row)

    return p
