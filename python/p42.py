#!/usr/bin/env python

from math import floor, sqrt

f = open ("../words.txt")

words = [x[1:-1] for x in f.readline().split(',')]

def is_triangle(t):
    a = .5
    b = .5
    c = -t
    r = sqrt(b**2 - 4*a*c)

    x = (-b + r) / 2 / a
    y = (-b - r) / 2 / a
    return floor(x) == x or floor(y) == y

def l_val(l):
    return ord(l.lower()) - ord('a') + 1

def word_val(w):
    return sum((l_val(l) for l in w))

print sum((1 for w in words if is_triangle(word_val(w))))
