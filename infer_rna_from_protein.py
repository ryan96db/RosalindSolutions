
from itertools import permutations


#protein = input("Enter Protein sequence:\n")

#codons = [rna[x:x+3] for x in range(0, len(rna), 3)]

#print(codons)

#protein_sequence = ""
z = ()
rnas = 0

def possible_codons(protein):
    possible_codons = []
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
        'UAC':'Y', 'UAU':'Y', 'UAA':'', 'UAG':'', 
        'UGC':'C', 'UGU':'C', 'UGA':'', 'UGG':'W', 
    }
    
    for aa in protein:
        for k, v in amino_acids.items():
            if v == aa:
                possible_codons.append(k)
    return possible_codons
       
#for codon in codons:
aminos = 'M'
z = possible_codons(aminos)

print(z)
perm = permutations(z, len(aminos))
for x in list(perm):
    rnas += 1
    
print(rnas)

#print("Protein Sequence: \n" + protein_sequence)