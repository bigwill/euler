#!/usr/bin/env python

from collections import deque
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

ps = set([])
for n in xrange(1, 1000000+1):
    if is_prime(n):
        ps.add(n)

def rotations(x):
    digits = deque(str(x))
    for x in xrange(len(digits)):
        digits.rotate(1)
        yield int(''.join([d for d in digits]))

c = 0
for p in ps:
    is_circular = True
    for r in rotations(p):
        if r not in ps:
            is_circular = False
            break
    if is_circular:
        c += 1

print c
