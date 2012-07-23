#!/usr/bin/env python

dmap = { 0:31,
         1:28,
         2:31,
         3:30,
         4:31,
         5:30,
         6:31,
         7:31,
         8:30,
         9:31,
         10:30,
         11:31
         }

m = 0
d = 0
y = 1900

def isleap(y):
    return y % 4 == 0 and (not y % 100 == 0 or y % 400 == 0)

def leapday(y, m):
    if isleap(y) and m == 1:
        return 1
    else:
        return 0

dow = 2 # Jan 1, 1901 was a Tuesday
sunc = 0 # Sunday count
for y in range(1901, 2000+1):
    for m in range(0, 11+1):
        for d in range(0, 30+1):
            if d >= (dmap[m] + leapday(y, m)):
                continue
            dow += 1
            dow %= 7
            if dow == 0 and d == 0:
                sunc += 1

print sunc
