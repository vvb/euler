#!/usr/bin/env python


def get_sum_of_multiple_of_3_and_5(n):
    total = 0
    for i in range(1, n):
        if (i % 3 == 0) or (i % 5 == 0):
            total += i
    return total

print(get_sum_of_multiple_of_3_and_5(1000))
