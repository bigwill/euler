#!/usr/bin/env python

from math import sqrt

# Basically jacked from: http://www.daniweb.com/software-development/python/code/216880
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in xrange(3, int(sqrt(n))+1, 2):
        if n % x == 0:
            return False
    return True

c = 0
x = 2

while True:
    if is_prime(x):
        c += 1
        if c == 10001:
            print x
            break
    x += 1
