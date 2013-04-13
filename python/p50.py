#!/usr/bin/env python

def loadprimes():
    with open("../primes1000000.txt") as f:
        return sorted([int(x) for x in f.xreadlines()], reverse=True)

def cumes(xs):
    s = 0
    l = []
    for x in xs:
        s += x
        l.append(s)
    return l

ps = loadprimes()
cps = cumes(ps)
l = len(ps)
h = {}

for p in ps:
    h[p] = True

a = None
max = 0

for i in xrange(0, l):
    for j in xrange(i+1, l):
        s = cps[j] - cps[i]
        if s >= 1000000:
            break
        if s in h and j-i > max:
            a = s
            max = j-i

print a
