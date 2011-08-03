#!/usr/bin/env python

s = set([])

for a in xrange(2, 100+1):
    for b in xrange(2, 100+1):
        s.add(a**b)

print len(s)
