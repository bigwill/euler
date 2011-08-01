#!/usr/bin/python

def is_divisible_list(x, ys):
    for y in ys:
        if x % y != 0:
            return False
    return True

def positives():
    x = 1
    while True:
        yield x
        x += 1

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for x in positives():
    if is_divisible_list(x, l):
        print x
        break
