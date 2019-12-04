# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:43:21 2019

@author: rdebo2
"""

#Reads .txt file and puts each sequence in a dictionary
seqdict = dict()

with open('rosalind_lcsm.txt') as file:
    for line in file:
        if ">Rosalind_" in line:
            key = line.strip()[1:]
            seqdict.setdefault(key, list())
        else:
            seqdict[key].append(line.strip())


result = dict()
for key, vlist in seqdict.items():
    result[key] = "".join(vlist)

#Length of dictionary and first DNA Sequence as a Reference
dict_length = len(result)
first_seq = list(result.values())[0]
first_seq_length = len(first)

sol = ""

for x in range(first_seq_length):
    for y in range(x + 1, first_seq_length + 1):
        #Gets all possible substrings of first DNA Sequence
        #Gets characters of string between x inclusive and y exclusive
        subs = first_seq[x:y]
        z = 1
        for z in range(1, dict_length):
            #See if substring is common to all sequences
            if subs not in list(result.values())[z]:
                break
        
        
        # If current substring is present in all sequences and its
        # length is greater than the current solution
        if (z + 1 == dict_length and len(sol) < len(subs)):
            sol = subs

print(sol)




#https://www.geeksforgeeks.org/longest-common-substring-array-strings/
