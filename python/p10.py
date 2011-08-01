#!/usr/bin/env python

nums = [x for x in xrange(0, 2000000)]

nums[0] = None
nums[1] = None

for x in xrange(0, 2000000):
    if not nums[x]:
        continue
    for i in xrange(2*x, 2000000, x):
        nums[i] = None

print sum((x for x in nums if x))
