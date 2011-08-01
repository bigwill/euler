#!/usr/bin/env python

def fib():
    (a, b) = (1, 1)
    while True:
        yield a
        (a, b) = (b, a + b)

t = 1
for x in fib():
    s = str(x)
    if len(s) >= 1000:
        print t
        break
    t += 1
