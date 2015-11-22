#!/usr/bin/env python

from itertools import takewhile
from math import sqrt

def naturals():
	i = 1
	while True:
		yield i
		i += 1

def triangles():
	s = 0
	for x in naturals():
		s += x
		yield s

dmap = {}
def divisors(x):
	if x in dmap:
		return dmap[x]
	fs = set()
	for y in xrange(1, int(sqrt(x)+1)):
		if x % y == 0:
			if x in dmap:
				fs.update(dmap[x])
			else:
				fs.add(y)
			if x/y in dmap:
				fs.update(dmap[x/y])
			else:
				fs.add(x/y)
	dmap[x] = fs
	return fs

for t in triangles():
	if len(divisors(t)) > 500:
		print t
		break
