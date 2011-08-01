#!/usr/bin/env python

from itertools import ifilter, takewhile

def fib():
    (a, b) = (1, 2)
    while True:
        yield a
        (a, b) = (b, a + b)

print sum(ifilter(lambda x : x % 2 == 0, takewhile(lambda x : x < 4000000, fib())))
