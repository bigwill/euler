#!/usr/bin/env python

def is_decimal_palindrome(n):
    return n == int(''.join(reversed(str(n))))

def is_bin_palindrome(n):
    b = bin(n)[2:]
    return b == ''.join(reversed(b))

print sum((n for n in xrange(1, 1000000) if is_decimal_palindrome(n) and is_bin_palindrome(n)))
