#!/usr/bin/env python


def fibo(n):
    x = 0
    y = 1
    fib = []
    if n == 0:
        return fib
    elif n == 1:
        fib.append(0)
        return fib
    elif n == 2:
        fib.append(0)
        fib.append(1)
        return fib
    fib.append(0)
    fib.append(1)
    for i in range(2, n):
        z = x + y
        x = y
        y = z
        fib.append(z)
        if z > 4000000:
            print("Exceeded", i)
    return fib

total = 0
for i in fibo(34):
    if i % 2 == 0:
        total += i
print(total)

