
rna = input("Enter RNA sequence:\n")

codons = [rna[x:x+3] for x in range(0, len(rna), 3)]

print(codons)

protein_sequence = ""

def translate_codon(codon):
    amino_acids = { 
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
        'AUG':'M', 
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
    for k, v in amino_acids.items():
        if k == codon:
            protein = v
    
    
    return protein
       
for codon in codons:
    protein_sequence += translate_codon(codon)

print("Protein Sequence: \n" + protein_sequence)
