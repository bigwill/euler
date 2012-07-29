#!/usr/bin/env python

import sys

from itertools import permutations
from math import sqrt

# Basically jacked from: http://www.daniweb.com/software-development/python/code/216880
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in xrange(3, int(sqrt(n))+1, 2):
        if n % x == 0:
            return False
    return True

def pandigitals(d):
    return (int(''.join([str(y) for y in x])) for x in permutations(range(1, d+1)))

p = None
for d in xrange(9, 0, -1):
    for x in pandigitals(d):
        if is_prime(x):
            if x > p:
                p = x
    if p:
        print p
        break
