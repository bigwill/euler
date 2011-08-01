#!/usr/bin/env python

import sys

def is_pythagorean_triplet(a, b, c):
    return a*a + b*b == c*c

for c in xrange(0, 1000+1):
    for b in xrange(0, c):
        for a in xrange(0, b):
            if is_pythagorean_triplet(a, b, c) and sum([a, b, c]) == 1000:
                print a*b*c
                sys.exit(0) # problem statement says there's exactly one
