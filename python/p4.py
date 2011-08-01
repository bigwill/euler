#!/usr/bin/env python

def palindromes():
    for x in xrange(999, 100, -1):
        for y in xrange(999, 100, -1):
            r = str(x*y)
            if r == r[::-1]:
                yield int(r)

print max(palindromes())
