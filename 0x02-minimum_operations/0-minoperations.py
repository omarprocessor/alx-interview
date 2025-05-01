#!/usr/bin/python3
"""
This module contains a function that computes the fewest number of
operations needed to get exactly n 'H' characters using only
Copy All and Paste.
"""


def minOperations(n):
    """Returns the minimum number of operations to get n H characters"""
    if n < 2:
        return 0

    ops = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            ops += divisor
            n //= divisor
        divisor += 1

    return ops
