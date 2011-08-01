#!/usr/bin/env python

def fib():
    (a, b) = (1, 2)
    while True:
        yield a
        (a, b) = (b, a + b)

def fib_below_4m():
    for x in fib():
        if x > 4000000:
            break
        yield x

print sum((x for x in fib_below_4m() if x % 2 == 0))
