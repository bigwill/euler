#!/usr/bin/env python

import sys

def pentagonal(n):
    return n * (3*n - 1) / 2

pentas_by_n = {}
pentas = set([])
max_penta = 0

for i in xrange(1, 10000001):
    pentas_by_n[i] = pentagonal(i)
    pentas.add(pentas_by_n[i])
    max_penta = pentas_by_n[i]

for j in xrange(1, 10000):
    for k in xrange(j, 10000):
        S = pentas_by_n[j] + pentas_by_n[k]
        assert S <= max_penta, 'number (%i) exceeds highest calculated pentagonal (%i)' % (S, max_penta)
        if S in pentas:
            D = abs(pentas_by_n[j] - pentas_by_n[k])
            assert D <= max_penta, 'number (%i) exceeds highest calculated pentagonal (%i)' % (D, max_penta)

            if D in pentas:
                print D
                sys.exit(0)
            
