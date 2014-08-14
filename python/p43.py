#!/usr/bin/env python

from itertools import permutations

pan_matches = set([])

for pan in permutations(xrange(0, 10)):
    pan_str = ''.join((str(d) for d in pan))
    pan_int = int(pan_str)
    match = True

    for (i, prime) in enumerate([2, 3, 5, 7, 11, 13, 17]):
        i += 1
        pan_sub = int(pan_str[i:i+3])
        if pan_sub % prime != 0:
            match = False
            break

    if match:
        pan_matches.add(pan_int)

print sum(pan_matches)
