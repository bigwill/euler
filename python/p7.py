#!/usr/bin/env python

def prime_factors(n):
    fs = []
    p = 2
    while n > 1:
        if n % p == 0:
            fs.append(p)
            n /= p
        else:
            p += 1
    return fs

c = 0
x = 2

while True:
    if len(prime_factors(x)) == 1:
        c += 1
        if c == 10001:
            print x
            break
    x += 1
