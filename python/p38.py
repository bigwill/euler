#!/usr/bin/env python

def is_pandigital(n):
    digits = dict(((x,False) for x in range(1, 10)))
    if len(str(n)) != 9:
        return False
    for d in str(n):
        d = int(d)
        if d not in digits:
            return False
        if digits[d]:
            return False
        digits[d] = True
    for x in digits.values():
        if not x:
            return False
    return True

pd = 0
for n in xrange(1, 500000):
    for z in xrange(1, 9 / len(str(n)) + 1):
        x = int(''.join([str(n*i) for i in xrange(1, z+1)]))
        if x > 987654321:
            break
        if is_pandigital(x) and x > pd:
            pd = x

print pd
