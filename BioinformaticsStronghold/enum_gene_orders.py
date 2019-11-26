# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:31:16 2019

@author: rdebo2
"""

from itertools import permutations

x = 7

perm = permutations(x)

for x in list(perm):
    print(x)