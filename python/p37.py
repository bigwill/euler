#!/usr/bin/env python

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

def truncations(n):
    s = str(n)
    l = len(s)
    for i in xrange(1, l):
        yield int(s[i:])
    for i in xrange(-1, -l, -1):
        yield int(s[:i])

tps = []
n = 11
while len(tps) < 11:
    if is_prime(n):
        truncable = True
        for t in truncations(n):
            if not is_prime(t):
                truncable = False
                break
        if truncable:
            tps.append(n)
    n += 1

print sum(tps)
