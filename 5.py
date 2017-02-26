#!/usr/bin/env python

divide_by = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def is_divisible(num):
    for each in divide_by:
        if num % each != 0:
            return False
    return True


num = 1
while True:
    if is_divisible(num):
        break
    num += 1

print(num)
