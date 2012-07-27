dmap = {}

def divisors(n):
    if n == 1:
        return set([1])
    if n in dmap:
        return dmap[n]

    divs = set([])

    for x in xrange(1, n/2+1):
        if x in divs:
            continue
        if n % x == 0:
            divs.add(x)
            divs.update(divisors(x))

    dmap[n] = divs
    return divs

def is_abundant(n):
    return sum(divisors(n)) > n

abuns = []

for x in range(1, 28123):
    if is_abundant(x):
        abuns.append(x)

ns = set(range(1, 28123+1))
for x in abuns:
    for y in abuns:
        s = x + y
        if s in ns:
            ns.remove(s)

print sum(ns)
