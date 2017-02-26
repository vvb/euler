#!/usr/bin/env python

num = 100
sum = 0
sum_of_sqaures = 0

for i in range(1, num+1):
    sum += i
    sum_of_sqaures += i*i

print sum*sum - sum_of_sqaures
