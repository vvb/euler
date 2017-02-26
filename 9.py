#!/usr/bin/env python


def is_pythagorean_triplet(x, y, z):
    if x*x + y*y == z*z:
        return True


def find_triplets(num):
    for i in range(1, num):
        for j in range(1, num):
            for k in range(1, num):
                if i*i + j*j == k*k:
                    if i+j+k == 1000:
                        print(i*j*k)
                        break

find_triplets(1000)
