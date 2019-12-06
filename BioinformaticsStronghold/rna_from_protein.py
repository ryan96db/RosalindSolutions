# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 15:45:20 2019

@author: rdebo2
"""
m, w, = (1, 1)
c, d, e, f, h, k, n, q, y = (2, 2, 2, 2, 2, 2, 2, 2, 2)
i = 3
a, g, l,p, r, s, t, v = (4, 4, 4, 4, 4, 4, 4, 4)
stop = 3

result = 0
amino_freq = {'A': a, 'C': c, 'D': d, 'E': e, 'F': f, 'G': g,
              'H': h, 'I': i, 'K': k, 'L': l, 'M':m, 'N': n,
              'P': p, 'Q': q, 'R': r, 'S': s, 'T': t, 'V': v,
              'W': w, 'Y': y}
print(amino_freq)

#with open('rosalind_mrna.txt', 'r') as file:
#seq = file.read()
seq = "MA"
print(seq)

for k, v in amino_freq.items():
    for amino in seq:
        if k in seq:
            result *= v

result *= stop

print(result)