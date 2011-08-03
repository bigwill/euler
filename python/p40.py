#!/usr/bin/env python

def positives():
    p = 1
    while True:
        yield p
        p += 1

def orders():
    o = 1
    c = 1
    for p in positives():
        for d in str(p):
            if c == o:
                yield int(d)
                o *= 10
            c += 1

i = 0
p = 1
for x in orders():
    p *= x
    if i == 6:
        break
    i += 1

print p
