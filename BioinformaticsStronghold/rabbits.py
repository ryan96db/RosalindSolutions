# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:04:55 2019

@author: rdebo2
"""

from scipy.special import comb

arr = []
with open('rosalind_fib.txt') as file:
    arr= [int(y) for y in file.read().split()]

n = arr[0]
k = arr[1]

def fib(months, pairs):
    
    
    if months == 1:
        return 1
    elif months == 2:
        return pairs
    
    else:
        genOne = fib(months-1, pairs)
        genTwo = fib(months-2, pairs)
    
    if months <=4:
        return (genOne + genTwo)
    
    return (genOne + (genTwo * pairs))

result = fib(n, k)
print(result)