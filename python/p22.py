#!/usr/bin/env python

alphabet = 'abcdefghijklmnopqrstuvwxyz'

f = open("../names.txt")
names = [x[1:-1] for x in f.read().split(',')]
f.close()

names.sort()

def alphascore(l):
    return alphabet.index(l.lower()) + 1

def wordscore(w):
    return sum((alphascore(l) for l in w))

i = 1
s = 0
for n in names:
    s += wordscore(n) * i
    i += 1

print s
