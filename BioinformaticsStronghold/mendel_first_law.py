# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:04:55 2019

@author: rdebo2
"""

from scipy.special import comb

arr = []
with open('rosalind_iprb.txt') as file:
    arr= [int(y) for y in file.read().split()]

k = arr[0]
m = arr[1]
n = arr[2]



pop_total = k + m + n
combo_total = comb(pop_total, 2)

#All the possible combinations that have a dominant allele
valid_combo = comb(k, 2) + k*m + k*n + .5*m*n + .75*comb(m,2)


print(valid_combo/combo_total)
