#!/usr/bin/env python

fracs = []

def is_curious(d, n):
    [d_1, d_0] = [int(x) for x in str(d)]
    [n_1, n_0] = [int(x) for x in str(n)]

    if d_1 == n_0 and n_1 != 0 and float(d_0) / n_1 == float(d) / n:
        return True
    if d_0 == n_1 and n_0 != 0 and float(d_1) / n_0 == float(d) / n:
        return True
    return False

for d in xrange(10, 100):
    for n in xrange(10, d):
        if is_curious(d, n):
            fracs.append((n, d))
            if len(fracs) == 4:
                break

big_n = 1
big_d = 1

for (n, d) in fracs:
    big_n *= n
    big_d *= d

print (big_n, big_d)
