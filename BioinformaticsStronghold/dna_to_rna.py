
dna = input("Enter DNA sequence (Maximum 1000 nucleotides):\n")

for nucleotide in dna:
    if nucleotide == "T":
        rna = dna.replace("T", "U")

print(rna)

    
       
