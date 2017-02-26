#!/usr/bin/env python
import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def find_primes(n):
    total = 0
    for x in xrange(2, n):
        if is_prime(x):
            total += x
    return total

print(find_primes(10))
print(find_primes(2000000))
