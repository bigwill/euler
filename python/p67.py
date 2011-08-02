#!/usr/bin/env python

f = open ("../p67_input.txt")

triangle = []

for l in f.xreadlines():
    l = l.rstrip()
    a = []
    for x in l.split(' '):
        a.append(int(x))
    triangle.append(a)

f.close()

def left((row, col)):
    return (row+1, col)

def right((row, col)):
    return (row+1, col+1)

def val((row, col)):
    return triangle[row][col]

for row in xrange(len(triangle)-2, -1, -1):
    for col in xrange(0, len(triangle[row])):
        p = (row, col)
        triangle[row][col] = val(p) + max(val(left(p)), val(right(p)))

print triangle[0][0]
