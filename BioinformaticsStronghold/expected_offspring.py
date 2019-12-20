# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:11:11 2019

@author: rdebo2
"""

import numpy as np

with open('rosalind_iev.txt') as file:
    data = file.read()

values_doubled = []

offspring = 0

orig = [int(x) for x in data.split()]



for y in orig:
    values_doubled.append(y * 2)

dataset = {
        'AA-AA': values_doubled[0],
        'AA-Aa': values_doubled[1],
        'AA-aa': values_doubled[2],
        'Aa-Aa': values_doubled[3],
        'Aa-aa': values_doubled[4],
        'aa-aa': values_doubled[5]
        }

    
gen_freq = {
        'AA-AA': 1.0,
        'AA-Aa': 1.0,
        'AA-aa': 1.0,
        'Aa-Aa': 0.75,
        'Aa-aa': 0.5,
        'aa-aa': 0
        }


result_dict = {
        
        'AA-AA': 1.0,
        'AA-Aa': 1.0,
        'AA-aa': 1.0,
        'Aa-Aa': 1.0,
        'Aa-aa': 1.0,
        'aa-aa': 1.0
        }

for k in dataset:
    if k in gen_freq:
        result_dict[k] = dataset[k] * gen_freq[k]

for key in result_dict:
    offspring += result_dict[key]

print(offspring)
