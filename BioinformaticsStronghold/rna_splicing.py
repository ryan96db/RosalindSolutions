# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:28:53 2019

@author: rdebo2
"""
#Reads .txt file and puts each sequence in a dictionary
seqdict = dict()

with open('rosalind_splc.txt') as file:
    for line in file:
        if ">Rosalind_" in line:
            key = line.strip()[1:]
            seqdict.setdefault(key, list())
        else:
            seqdict[key].append(line.strip())


result = dict()
for key, vlist in seqdict.items():
    result[key] = "".join(vlist)

def replicate(dna):
    compliments = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    compliment = "" .join(compliments.get(nucleotide) for nucleotide in reversed(dna))
    return compliment

def transcribe(dna):
    for nucleotide in dna:
        if nucleotide == "T":
            dna = dna.replace("T", "U")
    return dna

def codon_to_aa(codon):
    aa = ""
    amino_acids = { 
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T', 
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',                  
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P', 
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R', 
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A', 
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G', 
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S', 
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L', 
        'UAC':'Y', 'UAU':'Y', 'UAA':'69', 'UAG':'64', 
        'UGC':'C', 'UGU':'C', 'UGA':'65', 'UGG':'W', 
    }
    
    for k, v in amino_acids.items():
            if k == codon:
                aa = v
    return aa
                
def translate(rna):
    codons = [rna[x:x+3] for x in range(0, len(rna), 3)]
    amino_sequence = ""
    
    for codon in codons:
                amino_sequence += codon_to_aa(codon)

    return amino_sequence

for value in result:
    coding_strand = result[value]
    rna = transcribe(coding_strand)
    protein = translate(rna)
    print(protein)
    
    




        
    
    