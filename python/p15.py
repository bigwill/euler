#!/usr/bin/env python

grid = []

for x in xrange(0, 21):
    l = []
    for y in xrange(0, 21):
        l.append(0)
    grid.append(l)

for x in xrange(0, 21):
    for y in xrange(0, 21):
        if x == 0 and y == 0:
            ways = 1
        else:
            ways = 0

        if x > 0:
            ways += grid[x-1][y]
        if y > 0:
            ways += grid[x][y-1]
        grid[x][y] = ways

print grid[20][20]

for l in grid:
    print l
