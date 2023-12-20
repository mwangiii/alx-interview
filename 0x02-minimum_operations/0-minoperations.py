#!/usr/bin/python3
""" Calculates the minimum number of operations """


def minOperations(n):
    """ returns minimum operations """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
        else:
            divisor += 1

    return operations
