#!/usr/bin/env python

words = {1 : 'one',
         2 : 'two',
         3 : 'three',
         4 : 'four',
         5 : 'five',
         6 : 'six',
         7 : 'seven',
         8 : 'eight',
         9 : 'nine',
         10 : 'ten',
         11 : 'eleven',
         12 : 'twelve',
         13 : 'thirteen',
         14 : 'fourteen',
         15 : 'fifteen',
         16 : 'sixteen',
         17 : 'seventeen',
         18 : 'eighteen',
         19 : 'nineteen',
         20 : 'twenty',
         30 : 'thirty',
         40 : 'forty',
         50 : 'fifty',
         60 : 'sixty',
         70 : 'seventy',
         80 : 'eighty',
         90 : 'ninety',
         100 : 'hundred',
         1000 : 'thousand'
}

def word_len(x):
    digits = str(x)
    num_digits = len(digits)
    s = 0

    if num_digits >= 3 and int(digits[-2:]) != 0:
        s += len('and')

    for d in [int(x) for x in digits]:
        if d == 1 and num_digits == 2:
            kd = int(digits[-2:])
        else:
            if d == 1 and num_digits > 2:
                s += len('one')
            kd = d * 10**(num_digits-1)
        k1 = 10**(num_digits-1)

        if kd == 0:
            num_digits -= 1
            continue
        elif kd in words:
            s += len(words[kd])
            if d == 1 and num_digits == 2:
                break
        elif d in words and k1 in words:
            s += len(words[d]) + len(words[k1])
        else:
            raise Exception('faak=%s kd=%s k1=%s' % (d, kd, k1))
        num_digits -= 1

    return s

print sum((word_len(x) for x in xrange(1, 1000+1)))
