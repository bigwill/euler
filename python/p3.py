#!/usr/bin/env python

def prime_factors(n):
    p = 2
    while n > 1:
        if n % p == 0:
            yield p
            n /= p
        else:
            p += 1

print max(prime_factors(600851475143))
    
