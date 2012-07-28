#!/usr/bin/env python

import sys

n = 5
def spiral(n):
    M = []
    for r in range(0, n):
        m = []
        for c in range(0, n):
            m.append(0)
        M.append(m)

    x = n**2
    r = 0
    c = 0
    while x > 0:
        if x == 1:
            M[c][r] = 1
            break

        for i in range(c, n-1):
            M[i][r] = x
            x -= 1

        for j in range(r, n-1):
            M[n-1][j] = x
            x -= 1

        for i in range(n-1, c, -1):
            M[i][n-1] = x
            x -= 1

        for j in range(n-1, r, -1):
            M[c][j] = x
            x -= 1

        r += 1
        c += 1
        n -= 1

    return M

n = int(sys.argv[1])
S = spiral(n)
s = 0
for x in range(0, n):
    s += S[x][x]
for x in range(0, n):
    s += S[n-1-x][x]
s -= 1
print s
