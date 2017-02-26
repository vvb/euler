#!/usr/bin/env python

divide_by = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sum = 2*3*5*7*11*13*17*19


def is_divisible(num):
    for each in divide_by:
        if num % each != 0:
            return False
    return True

# since the number is divisible by all number until 20, it has to be a multiple
# of multipliers of all prime number until 20.
num = sum
while True:
    if is_divisible(num):
        break
    num += sum

print(num)
