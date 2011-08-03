#!/usr/bin/env python

def i(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n + 1

imap = {}

def seq_len(n):
    if n == 1:
        return 1
    elif n in imap:
        return imap[n]
    else:
        r = 1 + seq_len(i(n))
        imap[n] = r
        return r

max = 0
n = None
for x in xrange(1, 1000000):
    l = seq_len(x)
    if l > max:
        max = l
        n = x

print n
