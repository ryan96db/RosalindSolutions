# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:42:00 2019

@author: rdebo2
"""


complements = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
dna = input("Enter DNA sequence (Maximum 1000 base pairs):\n")
reverseCompliment = "" .join(complements.get(nucleotide) for nucleotide in reversed(dna))

print(reverseCompliment)



#complement = reverse(dna)

