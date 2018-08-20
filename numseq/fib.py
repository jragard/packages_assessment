"""Fibonacci related function"""


def fib(n):
    """Return nth Fibonacci number"""
    a, b = 0, 1
    c = a + b
    count = 0
    result = []

    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        while count < n:
            a = b
            b = c
            c = a+b
            count = count + 1
            result.append(c)
        return result[len(result) - 3]
