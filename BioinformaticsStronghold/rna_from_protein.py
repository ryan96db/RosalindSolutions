# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 15:45:20 2019

@author: rdebo2
"""
m, w, = (1, 1)
c, d, e, f, h, k, n, q, y = (2, 2, 2, 2, 2, 2, 2, 2, 2)
i = 3
l,s,r = (6,6,6)
a, g, p, t, v = (4, 4, 4, 4, 4)
stop = 3
result = 1

amino_freq = {'A': a, 'C': c, 'D': d, 'E': e, 'F': f, 'G': g,
              'H': h, 'I': i, 'K': k, 'L': l, 'M':m, 'N': n,
              'P': p, 'Q': q, 'R': r, 'S': s, 'T': t, 'V': v,
              'W': w, 'Y': y}
print(amino_freq)

#with open('rosalind_mrna.txt', 'r') as file:
#    seq = file.read()

print(seq)

for k in amino_freq:
    if k in seq:
        print(bool(k in seq))
        result = result * amino_freq[k]

result = result * stop
x = result % 1000000
print(x)
        

