#!/usr/bin/env python

from math import sqrt

def solutions(p):
    ss = []
    for a in xrange(1, p):
        for b in xrange(1, p-a):
            c = sqrt(a*a + b*b)
            if a + b + c == p:
                ss.append((a, b, c))
    return ss

max = 0
best_p = None

for p in xrange(1, 1000+1):
    slen = len(solutions(p))
    if slen > max:
        best_p = p
        max = slen

print best_p
