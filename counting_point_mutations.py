
dna1 = input("Enter two DNA sequences:\n")
dna2 = input()

hamming_distance = 0

for x in range(len(dna1)):
    if not (dna1[x] == dna2[x]):
        hamming_distance += 1

print(hamming_distance)

    
       
