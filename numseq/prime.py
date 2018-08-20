"""Functions dealing with prime numbers"""


def primes(n):
    """Return list of primes

    primes(n) returns a list of prime numbers less than n
    """
    results = []
    for num in range(2, n):
        prime = True
        for x in range(2, num):
            if num % x == 0:
                prime = False
            else:
                pass
        if prime:
            results.append(num)
    return results


def is_prime(m):
    """Determine if number is prime

    is_prime(m) takes a number as an argument and returns a boolean value True
    if m is a prime number, or False if m is not a prime number
    """
    prime = True
    for num in range(2, m):
        if m % num == 0:
            prime = False
        else:
            pass
    return prime
