# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:46:24 2019

@author: rdebo2
"""
#length = len(dna)

#Calculates the gc content of a single dna sequence
def calculate_gc(sequence):
    gcCount = float(0)
    gcPercentage = float(0)
    base_total = len(sequence)
    
    for nucleotide in sequence:
        if nucleotide == "C" or nucleotide == "G":
            gcCount += 1
            
        
        gcPercentage = (gcCount / base_total) * 100
        
    
    return gcPercentage

#Reads .txt file and puts each sequence in a dictionary
seqDict = dict()

with open('rosalind_gc.txt') as file:
    for line in file:
        if ">Rosalind_" in line:
            key = line.strip()[1:]
            seqDict.setdefault(key, list())
        else:
            seqDict[key].append(line.strip())

result = dict()
for key, vlist in seqDict.items():
    result[key] = "".join(vlist)

base_pair_percentages = []

#Calculates gc content of each sequence in dictionary
for value in result:
    #sequences = result[value]
    #print(sequences + "\n")
    #print(result[value] + "\n")
    dna = result[value]
    gcContent = calculate_gc(dna)
    result[value] = gcContent

highest_gc_id = max(result, key=result.get)

#Prints out Key and Value of DNA Sequence with highest GC Content
for k, v in result.items():
    if k == highest_gc_id:
        print(k)
        print(v)

file.close()


        




        
    



    



        
        
            
            
    


        

    
