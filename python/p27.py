#!/usr/bin/env python

from math import sqrt

# b has to be prime, so we just use this list to enumerate possibles
# b's as an efficiency hack
bs = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 
127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 
179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 
233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 
283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 
353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 
419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 
467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 
547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 
607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 
661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 
739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 
811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 
877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 
947, 953, 967, 971, 977, 983, 991, 997]

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

def primes_count(a, b):
    n = 0
    while True:
        if not is_prime(n*n + a*n + b):
            return n
        n += 1

def p27():
    max_pcnt = 0
    best_a = None
    best_b = None
    for a in xrange(-999, 1000):
        for b in bs:
            c = primes_count(a, b)
            if c > max_pcnt:
                max_pcnt = c
                best_a = a
                best_b = b
    return best_a*best_b

print p27()
