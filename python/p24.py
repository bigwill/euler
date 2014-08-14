#!/usr/bin/env python

from itertools import permutations

for (i, x) in enumerate(permutations('0123456789')):
    if i == 999999: # index of 1 millionth element
        print ''.join(x)
        break
