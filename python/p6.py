#!/usr/bin/env python

print sum(xrange(1, 100+1))**2 - sum((x*x for x in xrange(1, 100+1)))
