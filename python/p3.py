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

print max(prime_factors(600851475143))
    
