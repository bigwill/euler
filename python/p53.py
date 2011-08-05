#!/usr/bin/env python

from math import factorial

def choose(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

s = 0
for n in xrange(1, 100+1):
    for r in xrange(1, n+1):
        if choose(n, r) > 1000000:
            s += 1

print s
