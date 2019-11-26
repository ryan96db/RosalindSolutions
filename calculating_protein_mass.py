# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 10:58:59 2019

@author: rdebo2
"""


protein = input("Enter Protein sequence:\n")
protein_mass = 0

def calculate_protein_mass(aa):
    masses = { 
           'A': 71.03711,
           'C': 103.00919,
           'D': 115.02694,
           'E': 129.04259,
           'F':   147.06841,
           'G':   57.02146,
           'H':   137.05891,
           'I':   113.08406,
           'K':   128.09496,
           'L':   113.08406,
           'M':   131.04049,
           'N':   114.04293,
           'P':   97.05276,
           'Q':   128.05858,
           'R':   156.10111,
           'S':   87.03203,
           'T':   101.04768,
           'V':   99.06841,
           'W':   186.07931,
           'Y':   163.06333 ,
    } 
    for k, v in masses.items():
        if k == aa:
            mass = v
    
    
    return mass

for amino_acid in protein:
    protein_mass += calculate_protein_mass(amino_acid)

print(round(protein_mass,3))

       