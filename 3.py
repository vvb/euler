#!/usr/bin/env python

num = 600851475143
factors = []
exclude = []


def get_first_factor(num):
    for x in xrange(2, num):
        if num % x == 0:
            return x, num/x
    return None, None

x, y = get_first_factor(num)
factors.append(x)
factors.append(y)
for each in factors:
    x, y = get_first_factor(each)
    if x is None:
        continue
    factors.append(x)
    factors.append(y)
    exclude.append(each)

for each in exclude:
    factors.remove(each)
print(factors)
