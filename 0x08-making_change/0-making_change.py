#!/usr/bin/python3
""" Get minimum number of coins """


def makeChange(coins, total):
    """ Returns fewest numbers of coins """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    i = 0
    counter = 0

    for i in range(len(coins)):
        while (total >= coins[i]):
            total -= coins[i]
            counter += 1

    if total != 0:
        return -1

    return counter
