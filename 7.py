#!/usr/bin/env python


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def find_prime(num):
    count = 0
    x = 2
    while True:
        if is_prime(x):
            count += 1
            if count == num:
                print(x)
                break
        x += 1

find_prime(10001)
