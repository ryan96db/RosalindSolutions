# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:47:24 2020

@author: rdebo2
"""
import numpy as np


seqDict = dict()

x = []
twoArray = []

#Reads .txt file and puts each sequence in a dictionary
with open('rosalind_cons.txt') as file:
    for line in file:
        if ">Rosalind_" in line:
            key = line.strip()[1:]
            seqDict.setdefault(key, list())
        else:
            seqDict[key].append(line.strip())


#Creates one long string for each DNA Sequence    
result = dict()
for key, vlist in seqDict.items():
    result[key] = "".join(vlist)

#Adds the nucleotides of each DNA sequence to an array,
#and adds each resultant array into a 2D array
    

for k, v in result.items():
    for nuc in v:
        x.append(nuc)
    twoArray.append(x)
    x=[]

#Creates numpy array
a = np.array(twoArray)


#print(a[:,1])

#Gets length of DNA Sequences
def getSequenceLength():
    for ke, va in result.items():
        sequenceLength = len(va) 
    return sequenceLength

y = getSequenceLength()

#Fills profile with arrays of numbers equal to the length of the DNA strings
profile = {
        'A': [],
        'C': [],
        'G': [],
        'T': []
        }

def fillProfile():
    for g in range(y):
        profile['A'].append(0)
        profile['C'].append(0)
        profile['G'].append(0)
        profile['T'].append(0)

fillProfile()

    
#Makes a temporary array to get all nucleotides at a certain position,
#Then adds one to corresponding nucleotide in profile    
for h in range(y):
    tempArray = a[:,h]
    for nuc in tempArray:
        for k, v in profile.items():
            if nuc == k:
                profile[k][h] += 1
    tempArray = []

consensus = ""

defaultDict = {
        
        'A': 0,
        'C': 0,
        'G': 0,
        'T': 0
        
        }

#Creates a temporaray dictionary for the nucleotide values at a certain position,
#sees which values is the highest, and adds it to the consensus string
for j in range(y):
    
    temp = defaultDict
    
    adenine = profile['A'][j]
    cytosine = profile['C'][j]
    guanine = profile['G'][j]
    thymine = profile['T'][j]
    
    temp['A'] = adenine
    temp['C'] = cytosine
    temp['G'] = guanine
    temp['T'] = thymine
    
    
    consensus += max(temp, key=temp.get)
    
    temp.update(defaultDict)


print(consensus)   


#Prints out Profile in Format that problem asks for
def printOutProfile(prof):
    print('A:', end = ' ' )
    for b in range(y):
        print(profile['A'][b], end = " ")
    print("")
    
    print('C:', end = ' ' )
    for c in range(y):
        print(profile['C'][c], end = " ")
    print("")
    
    print('G:', end = ' ' )
    for d in range(y):
        print(profile['G'][d], end = " ")
    print("")
    
    print('T:', end = ' ' )
    for e in range(y):
        print(profile['T'][e], end = " ")
    print("")
    
        
    
printOutProfile(profile)
    
    
        
    




