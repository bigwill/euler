#!/usr/bin/env python

def divisors(n):
    if n == 1:
        yield 1

    for x in xrange(1, n/2+1):
        if n % x == 0:
            yield x

ds = [0]
dmap = {}

for x in xrange(1, 10000):
    ds.append(sum(divisors(x)))

for x in xrange(1, len(ds)):
    for y in xrange(x+1, len(ds)):
        if x == y:
            continue
        if ds[x] == y and x == ds[y]:
            dmap[x] = True
            dmap[y] = True

print sum(dmap.keys())

