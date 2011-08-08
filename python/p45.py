#!/usr/bin/env python

from math import sqrt

def t_n(n):
    return n * (n+1) / 2

def p_n_inv(p):
    return (1 + sqrt(24 * p + 1)) / 6.0

def h_n_inv(h):
    return (1 + sqrt(8 * h + 1)) / 4.0

def is_round(n):
    return (n - int(n)) == 0.0

n = 286
while True:
    t = t_n(n)
    if is_round(p_n_inv(t)) and is_round(h_n_inv(t)):
        print t
        break
    n += 1
