#!/usr/bin/python3
"""
Main file for the task
"""


def minOperations(n):
    """
    Return:
    sum of their prime factors of each number
    """
    if (n <= 1):
        return (0)
    mul = 2
    total = 0
    while (n != 1):
        if n % mul == 0:
            n /= mul
            total += mul
            mul = 2
        else:
            mul += 1
    return total


if __name__ == '__main__':
    minOperations(n)
