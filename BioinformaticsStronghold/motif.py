# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 13:39:53 2019

@author: rdebo2
"""

dna = input("Enter DNA sequence:\n")
motif = input("Enter DNA substring:\n")


def findMotif(seq, substring):
    instances = [seq[x:x+len(substring)] for x in range(0,len(seq))]
    #Finds all possible substrings of the length of the substring in question
    return [index for index, element in enumerate(instances) if element == substring]
#Gets the index of each element if the element matches the substring
    



cases = findMotif(dna, motif)
casesOfMotif = [x + 1 for x in cases]


print(casesOfMotif)
