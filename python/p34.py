#!/usr/bin/env python

from math import factorial

def boom(n):
    return n == sum((factorial(int(x)) for x in str(n)))

print sum((x for x in xrange(3, 1000000) if boom(x)))
